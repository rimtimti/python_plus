# Напишите программу, которая получает целое число и возвращает его двоичное, восьмеричное строковое представление.
# Функции bin и oct используйте для проверки своего результата, а не для решения.

# Дополнительно:
# Попробуйте избежать дублирования кода в преобразованиях к разным системам счисления
# Избегайте магических чисел
# Добавьте аннотацию типов где это возможно

import defs

MIN_NUMBER = 0
MAX_NUMBER = 2_147_483_647

number = defs.get_natural_int_between_number(
    f"Введите число от {MIN_NUMBER} до {MAX_NUMBER}: ", MIN_NUMBER, MAX_NUMBER
)
SYSTEM = 2
print(
    f"Число {number} в системе счисления {SYSTEM} = {defs.convert_number_to_number_system(number, SYSTEM)}",
    f"через встроенную функцию = {bin(number)[2:]}",
)
SYSTEM = 8
print(
    f"Число {number} в системе счисления {SYSTEM} = {defs.convert_number_to_number_system(number, SYSTEM)}",
    f"через встроенную функцию = {oct(number)[2:]}",
)
