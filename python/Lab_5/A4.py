
class Sequence:
    def __init__(self, line):
        s = line.replace('\n', '').split('\t')
        self.name = s[0]
        self.animal = s[1]
        self.chane = s[2]

class Command:
    def __init__(self, line, number):
        self.number = number
        s = line.replace('\n', '').split('\t')
        self.name = s[0]
        self.param1 = s[1]
        if len(s)>2:
            self.param2 = s[2]
        else:
            self.param2 = ""

    def GetNameLine(self):
        sNum =str(self.number)
        while len(sNum) < 3:
            sNum = "0"+sNum
        return sNum + "\t" + self.name +  "\t" + self.param1  +"\t" + self.param2


    def CompareChain(self, c1, c2 ):
        char_counts1 = {}
        for char in c1:
            char_counts1[char] = char_counts1.get(char, 0) + 1

        char_counts2 = {}
        for char in c2:
            char_counts2[char] = char_counts2.get(char, 0) + 1

        count = 0
        unique_to_dict1 = set(char_counts1.keys()) - set(char_counts2.keys())
        unique_to_dict2 = set(char_counts2.keys()) - set(char_counts1.keys())
        common_keys = set(char_counts1.keys()) & set(char_counts2.keys())
        for k in unique_to_dict1:
            count += char_counts1[k]

        for k in unique_to_dict2:
            count += char_counts2[k]

        for k in common_keys:
            v = char_counts2[k] - char_counts1[k]
            if v < 0:
                v = -v
            count +=v

        return str(count)

    def GetDataForMode(self, chain):
        res = []
        char_counts = {}
        for char in chain:
            char_counts[char] = char_counts.get(char, 0) + 1

        max_value = max(char_counts.values())
        max_keys = [key for key, value in char_counts.items() if value == max_value]
        sorted_keys = sorted(max_keys)

        for k in sorted_keys:
            res.append(k + "\t" + str(char_counts[k]))

        return res


    def Apply(self, seq):
        res = []
        res.append(self.GetNameLine())
        #print(self.GetNameLine())
        if self.name == "search":
            found = False
            for v in seq:
                #print(v.chane)
                if (v.chane.find(self.param1) != -1):
                    if not found:
                        res.append("organism \t protein")
                    found = True
                    res.append(v.animal + "\t" + v.name)
            if not found:
                res.append("NOT FOUND")
        elif self.name == "diff":
            seq1 = None
            seq2 = None
            for v in seq:
                if v.name == self.param1:
                    seq1 = v
                if v.name == self.param2:
                    seq2 = v

            if seq1 == None or seq2 == None:
                res.append("MISSING")
            else:
                res.append("amino - acids difference:")
                res.append(self.CompareChain(seq1.chane, seq2.chane))
        elif self.name == "mode":
            for v in seq:
                if v.name == self.param1:
                    seq1 = v

            if seq1 != None:
                res.append("amino-acid occurs:")
                res.extend(self.GetDataForMode(seq1.chane))

        res.append("--------------------------------------------------------------------------")
        return res

def AddHeader(data):
    data.append("Nikolay Maksimenko")
    data.append("Genetic Searching")
    data.append("--------------------------------------------------------------------------")

with open('d:\коля\Sequences.2.txt', 'r') as f:
    lines = f.readlines()
_seq = []
for l in lines:
    _seq.append(Sequence(l))

with open('d:\коля\Commands.2.txt', 'r') as f2:
    lines2 = f2.readlines()

_comm = []

n=0
for l in lines2:
    n = n+1
    _comm.append(Command(l, n))

_out =[]

AddHeader(_out)

for c in _comm:
    _out.extend(c.Apply(_seq))

with open('d:\коля\Generated.2.txt', "w") as file:
    for line in _out:
        file.write(line+"\n")