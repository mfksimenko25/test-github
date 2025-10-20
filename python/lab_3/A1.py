# Ввод координат двух точек
x1 = int(input("Введите x1: "))
y1 = int(input("Введите y1: "))
x2 = int(input("Введите x2: "))
y2 = int(input("Введите y2: "))

# Проверка, что координаты не равны 0
if x1 == 0 or y1 == 0 or x2 == 0 or y2 == 0:
    print("Координаты не должны быть равны 0")
else:
    # Определение четверти для первой точки
    if x1 > 0 and y1 > 0:
        quarter1 = 10
    elif x1 < 0 and y1 > 0:
        quarter1 = 2
    elif x1 < 0 and y1 < 0:
        quarter1 = 3
    elif x1 > 0 and y1 < 0:
        quarter1 = 4

    # Определение четверти для второй точки
    if x2 > 0 and y2 > 0:
        quarter2 = 1
    elif x2 < 0 and y2 > 0:
        quarter2 = 2
    elif x2 < 0 and y2 < 0:
        quarter2 = 3
    elif x2 > 0 and y2 < 0:
        quarter2 = 4

    # Сравнение четвертей
    if quarter1 == quarter2:
        print(f"YES: {quarter1}")
    else:
        print("NO")
