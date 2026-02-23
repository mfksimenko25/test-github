import math

f = lambda x: math.tan(0.2*x + 0.3) - x**2 + 2
df = lambda x: 0.2/(math.cos(0.2*x + 0.3)**2) - 2*x

def bisection(a, b, eps=0.01):
    for k in range(1, 101):
        c = (a+b)/2
        if abs(b-a) <= eps or abs(f(c)) <= eps: return c, k
        if f(a)*f(c) < 0: b = c
        else: a = c
    return (a+b)/2, 100

def newton(x0, eps=0.01):
    x = x0
    for k in range(1, 101):
        try:
            x_new = x - f(x)/df(x)
            if abs(x_new - x) <= eps or abs(f(x_new)) <= eps: return x_new, k
            x = x_new
        except: return None, k
    return x, 100

print("tg(0.2x+0.3)=x^2-2\n")
x, k = bisection(2, 3)
print(f"Бисекция [2,3]: x={x:.6f}, итераций={k}, f(x)={f(x):.6f}")
x, k = newton(2)
print(f"Ньютон x0=2: x={x:.6f}, итераций={k}, f(x)={f(x):.6f}")