# Пользователь вводит число от 1 до 999. Используя операции с числами
# сообщите что введено: цифра, двузначное число или трёхзначное число.
# Для цифры верните её квадрат, например 5 - 25
# Для двузначного числа произведение цифр, например 30 - 0
# Для трёхзначного числа его зеркальное отображение, например 520 - 25
# Если число не из диапазона, запросите новое число
# Откажитесь от магических чисел
# В коде должны быть один input и один print

import defs

MIN_NUMBER = 1
MAX_NUMBER = 999

number = defs.get_natural_int_between_number(
    f"Введите число от {MIN_NUMBER} до {MAX_NUMBER}: ", MIN_NUMBER, MAX_NUMBER
)
match len(str(number)):
    case 1:
        result = f"Вы ввели цифру. Квадрат этого числа равен: {number ** 2}"
    case 2:
        result = f"Вы ввели двузначное число. Произведение цифр этого числа равно: {(number % 10) * (number // 10)}"
    case 3:
        result = f"Вы ввели трёхзначное число. Зеркальное отображение цифр этого числа равно: {int(str(number)[::-1])}"
print(result)
