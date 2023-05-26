# Напишите программу, которая вычисляет площадь круга и длину окружности по введённому диаметру.
# Диаметр не превышает 1000 у.е.
# Точность вычислений должна составлять не менее 42 знаков после запятой.

import defs
import decimal
from math import pi

MIN_NUMBER = 0
MAX_NUMBER = 1_000
CALCULATION_ACCURACY = 42

def area_and_circumference_of_circle_from_diameter(number: decimal, accuracy: int) -> list[decimal, decimal]:
    '''
    Возвращает площадь и длину окружности с точностью accuracy после запятой
    '''
    decimal.getcontext().prec = accuracy
    return (decimal.Decimal(pi) * number ** 2) / 4, decimal.Decimal(pi) * number

print(f'Эта программа запрашивает диаметр круга и выдает его площать и длину окружности с точностью {CALCULATION_ACCURACY} знака после запятой.')
number = defs.get_decimal_between_number(f'Введите число от {MIN_NUMBER} до {MAX_NUMBER}: ', MIN_NUMBER, MAX_NUMBER)
array = area_and_circumference_of_circle_from_diameter(number, CALCULATION_ACCURACY)
print(f'Площадь круга с диаметром {number}          = {array[0]}')
print(f'Длина окружности круга с диаметром {number} = {array[1]}')