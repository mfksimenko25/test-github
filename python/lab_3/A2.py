# Ввод пароля
password = input("Введите пароль: ")

# Допустимые специальные символы
special_chars = {'*', '-', '#'}

# Флаги для проверки
errors = []

# Проверка длины
if len(password) != 8:
    errors.append("Длина пароля не равна 8")

# Проверка наличия заглавных букв
if not any(c.isupper() for c in password):
    errors.append("В пароле отсутствуют заглавные буквы")

# Проверка наличия строчных букв
if not any(c.islower() for c in password):
    errors.append("В пароле отсутствуют строчные буквы")

# Проверка наличия цифр
if not any(c.isdigit() for c in password):
    errors.append("В пароле отсутствуют цифры")

# Проверка наличия специальных символов
if not any(c in special_chars for c in password):
    errors.append("В пароле отсутствуют специальные символы")

# Проверка на недопустимые символы
allowed_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789") | special_chars
if any(c not in allowed_chars for c in password):
    errors.append("В пароле используются непредусмотренные символы")

# Вывод результата
if not errors:
    print("Надежный пароль")
else:
    for error in errors:
        print(error)