import random
import time
correct_answers = 0
total_time = 0
question_times = []
n = int(input("Введите количесвто примеров N "))
for i in range(1, n + 1):
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        correct = a * b

        while True:
            print(f"Вопрос {i}/{n} ")
            print(f"{a} × {b} = ")
            start = time.time()
            user_input = input()
            end = time.time()

            try:
                answer = int(user_input)
                elapsed = round(end - start, 2)

                question_times.append(elapsed)
                total_time += elapsed
                if answer == correct:
                    correct_answers += 1
                    print(f" Верно!.(Время: {elapsed} сек)")
                else:
                    print(f" Неверно! Правильно: {correct} (Время: {elapsed} сек)")
                break
            except ValueError:
                print("Пожалуйста, введите целое число.\n")

average_time = round(total_time / n, 2)
accuracy = round((correct_answers / n) * 100, 2)
print(" =============================================")
print(" СТАТИСТИКА:")
print(" =============================================")
print(f" Общее время: {round(total_time, 2)} сек.")
print(f" Среднее время на вопрос: {average_time} сек.")
print(f" Правильных ответов: {correct_answers} из {n}")
print(f" Процент правильных: {accuracy}%")