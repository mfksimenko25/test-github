def gettype(num):
    if num[0] == 4:
        return 1
    if num[0] == 5 and num[1] >= 1 and num[1] <= 5  :
        return 2
    if num[0] == 3 and (num[1] == 4 or num[1] == 7):
        return 3
    return -1


def checklen (num, type):
    l=len(num)
    if type == 1 and (l == 13 or l == 16):
        return True
    if type == 2 and l == 16:
        return True
    if type == 3 and l == 15 :
        return True
    return False


def loon (num):
    s=0
    chet=False
    for i in reversed(num):
        if chet:
            n = i*2
            if n>9:
                n=n-9
            s = s+n
        else:
            s = s+i

        chet=not chet
    return s%10==0




card_types = ["visa", "MasterCard", "American Express"]
cardst = str(input(" "))
numbers = [int(char) for char in cardst]
ct=gettype(numbers)
if ct != -1 and checklen(numbers, ct) and loon(numbers):
   print(card_types[ct-1])
else:
    print("Invalid")
