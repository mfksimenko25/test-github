def rect(n, m):
    print(f"ПРЯМОУГОЛЬНИК {n}x{m}:")
    for i in range(1, n + 1):
        s=""
        for j in range(1, m + 1):
            s+="#"
        print (s)

def triangle (n, m):
    print(f"ПРАВЫЙ ТРЕУГОЛЬНИК {n}x{m}:")
    for i in range(1, n + 1):
        s=""
        for j in range(1, m + 1):
            if i>=j and i<=m:
                s+="#"

        print (s)

def frame (n, m):
    print(f"РАМКА {n}x{m}:")
    for i in range(1, n + 1):
        s=""
        for j in range(1, m + 1):
            if i==1 or j==1 or i==n or j==m:
                s+="#"
            else:
                s += " "
        print (s)


n = int(input("Введите количесвто  n "))
m = int(input("Введите количесвто  m "))
rect (n, m)
triangle (n, m)
frame(n, m)