# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

import defs

MIN_NUMBER = 0
MAX_NUMBER = 2_147_483_647
SYSTEM = 16

number = defs.get_natural_int_between_number(
    f"Введите число от {MIN_NUMBER} до {MAX_NUMBER}: ", MIN_NUMBER, MAX_NUMBER
)

print(
    f"Число {number} в системе счисления {SYSTEM} = {defs.convert_number_to_number_system(number, SYSTEM)}",
    f"через встроенную функцию = {hex(number)[2:]}",
)
