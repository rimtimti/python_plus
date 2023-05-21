# Напишите программу, которая запрашивает год и проверяет его на високосность.
# Распишите все возможные проверки в цепочке elif
# Откажитесь от магических чисел
# Обязательно учтите год ввода Григорианского календаря
# В коде должны быть один input и один print
import defs

START_YEAR = 1582
CHECK_LEAP_YEAR_1 = 4
CHECK_LEAP_YEAR_2 = 100

MIN_YEAR = 0
MAX_YEAR = 2147483647

year = defs.get_natural_int_between_number('Введите год в формате yyyy: ', MIN_YEAR, MAX_YEAR)
result = " не високосный"
if year % CHECK_LEAP_YEAR_1 == 0 and year % CHECK_LEAP_YEAR_2 != 0 or year % (CHECK_LEAP_YEAR_2 * CHECK_LEAP_YEAR_1) == 0:
    result = " високосный"
if year < START_YEAR:
    result = ", когда григорианский календарь еще не существовал..."
print("Это год" + result)
