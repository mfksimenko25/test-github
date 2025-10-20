# Ввод показаний
prev = int(input("Предыдущее показание: "))
curr = int(input("Текущее показание: "))

# Учёт перехода через 9999
if curr >= prev:
    used = curr - prev
else:
    used = (10000 - prev) + curr

# Расчёт стоимости
if used <= 300:
    cost = 21.00
elif used <= 600:
    cost = 21.00 + (used - 300) * 0.06
elif used <= 800:
    cost = 21.00 + 300 * 0.06 + (used - 600) * 0.04
else:
    cost = 21.00 + 300 * 0.06 + 200 * 0.04 + (used - 800) * 0.025

# Средняя цена за кубометр
average_price = cost / used if used > 0 else 0

# Вывод результатов
print(f"Использовано: {used} кубометров")
print(f"Сумма оплаты: {cost:.2f} $")
print(f"Средняя цена за кубометр: {average_price:.2f} $")