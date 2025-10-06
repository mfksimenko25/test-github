# Ввод координат первой и второй клетки
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

# Если сумма чётная — белая, если нечётная — чёрная
color1 = (x1 + y1) % 2
color2 = (x2 + y2) % 2

# Проверка на совпадение цветов
same_color = (color1 == color2)

# Вывод результата
print("YES" if same_color else "NO")

# Если цвета совпадают — выводим их цвет
if same_color:
    print("White" if color1 == 0 else "Black")
