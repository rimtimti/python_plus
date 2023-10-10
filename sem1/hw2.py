# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: «Число является простым, если делится нацело только на единицу
# и на себя». Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

import defs

MIN_NUMBER = 1
MAX_NUMBER = 100_000

number = defs.get_natural_int_between_number(
    f"Введите натуральное число от {MIN_NUMBER} до {MAX_NUMBER}: ",
    MIN_NUMBER,
    MAX_NUMBER,
)
array = defs.get_multipliers_number(number)

match len(array):
    case 1:
        result = "Число 1 не имеет простых делителей и не является ни простым, ни составным числом."
    case 2:
        result = "Число простое."
    case _:
        result = "Число составное."

print(result)
