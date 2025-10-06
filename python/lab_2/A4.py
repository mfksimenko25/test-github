# Считываем два целых числа от 1 до 1000
A = int(input())
B = int(input())

# Используем формулу: max = (A + B + abs(A - B)) // 2

max_value = (A + B + (A - B) * ((A - B) // abs(A - B))) // 2

print(max_value)