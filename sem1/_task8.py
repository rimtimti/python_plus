# Нарисовать в консоли ёлку спросив у пользователя количество рядов.
# Сколько рядов у ёлки?
#     *
#    ***
#   *****
#  *******
# *********

import defs

MIN_NUMBER = 0
MAX_NUMBER = 50

count = defs.get_natural_int_between_number(
    "Программа рисует елочку. На экран терминала влезет только 50 рядов. Сколько рядов у ёлки?: ",
    MIN_NUMBER,
    MAX_NUMBER,
)

for i in range(count):
    print(" " * (count - 1 - i) + "*" * (i * 2 + 1))
