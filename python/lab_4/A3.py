def Maxlost1 (packets):
    maxstr = 0
    a=packets.split('1')
    for str in a:
        if len(str) > maxstr:
            maxstr = len(str)
    return maxstr

def Maxlost2 (packets):
    lost = 0
    maxlost = 0
    b = False
    for char in packets:
        if char == '0':
            lost += 1
            b = True
        else:
            if b:
                if lost > maxlost:
                    maxlost = lost
                b = False
            lost = 0

    if b:
        if lost > maxlost:
            maxlost = lost
        b = False

    return maxlost

def Netstatus(per):
    if per<=1:
        return "Отличное качество"

    if per<5:
        return "Хорошее качество"

    if per<10:
        return "Удовлетворительное качество"

    if per<20:
        return "Плохое качество"
    return "Критическое состояние сети"



print ("Ввод:")
packets =""
while True:
    packets = str(input(" "))
    if not all(char in '01' for char in packets):
        print("Неверный ввод. Используйте только символы '0' и '1'!")
    else:
        if len(packets)<5:
            print ("Длина должна быть не меньше 5")
        else:
            break

lostcount=packets.count('0')
count=len(packets)
percent=lostcount*100/count
maxlost = Maxlost2(packets)
print("Вывод:")
print(f"Общее количество пакетов:{count}")
print(f"Количество потерянных пакетов:{lostcount}")
print(f"Длина самой длинной последовательности потерянных пакетов:{maxlost}")
print(f"Процент потерь:{round(percent, 2)}%")
print(f"Качество связи:{Netstatus(percent)}")



