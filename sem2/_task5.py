# Напишите программу, которая решает квадратные уравнения даже если дискриминант отрицательный.
# Используйте комплексные числа для извлечения квадратного корня.

import defs

ACCURACY = 14

def solve_quadratic_equation(array: list) -> print():
    '''
    Решает уравнение вида a*x² + b*x + c = 0
    '''
    a = array[0]
    b = array[1]
    c = array[2]
    discriminant = round(b ** 2 - 4 * a * c, ACCURACY)
    print(f'Дискриминант = {discriminant}')
    x1 = (-b + discriminant ** 0.5) / (2 * a)
    x2 = (-b - discriminant ** 0.5) / (2 * a)
    if discriminant < 0:
        x1 = complex(round(x1.real, ACCURACY), round(x1.imag, ACCURACY))
        x2 = complex(round(x2.real, ACCURACY), round(x2.imag, ACCURACY))
    print(f'x1 = {x1}')
    if discriminant != 0:
        print(f'x2 = {x2}')


print('Решаем уравнение вида a*x² + b*x + c = 0')
array = defs.get_array_float_number_required_size('Введите значение a, b и c через запятую: ', 3)
solve_quadratic_equation(array)