import decimal

def get_natural_int_between_number(text: str, number_min: int, number_max: int) -> int:
    '''
    Просит у пользователя ввести целое число между min и max и проверяет ввод
    '''
    try:
        number_int = int(input(text))
        if number_int >= number_min and number_int <= number_max:
            return number_int
        else:
            print('Неверный ввод числа!!!')
            return get_natural_int_between_number(text, number_min, number_max)
    except ValueError:
        print('Неверный ввод числа!!!')
        return get_natural_int_between_number(text, number_min, number_max)


def get_decimal_between_number(text: str, number_min: decimal, number_max: decimal) -> decimal:
    '''
    Просит у пользователя ввести целое число между min и max и проверяет ввод
    '''
    try:
        number_decimal = decimal.Decimal(input(text))
        if number_decimal >= number_min and number_decimal <= number_max:
            return number_decimal
        else:
            print('Неверный ввод числа!!!')
            return get_decimal_between_number(text, number_min, number_max)
    except ValueError:
        print('Неверный ввод числа!!!')
        return get_decimal_between_number(text, number_min, number_max)


def get_multipliers_number(number: int) -> list[int]:
    '''
    Выдает все множители натурального числа
    '''
    array_multipliers = []
    for i in range(1, number+1):
        if number % i == 0:
            array_multipliers.append(i)
            number /= i
    return array_multipliers


def get_array_float_number_required_size(text: str, size: int) -> list[float]:
    '''
    Просит у пользователя ввести нужное количество float чисел, проверяет это
    '''
    try:
        array = input(text).strip().split(',')
        if len(array) == size:
            for i in range(len(array)):
                array[i] = float(array[i])
            return array
        else:
            print('Неверный ввод!!!')
            return get_array_float_number_required_size(text, size)
    except ValueError:
        print('Неверный ввод!!!')
        return get_array_float_number_required_size(text, size)


def view_table_multiplication(start: int, finish: int, min_number: int, max_number: int, step_user: int) -> print:
    '''
    Рисует классическую таблицу умножения от start по finish с кол-вом столбцов step_user на странице терминала, умножает на числа от min_number до max_number
    '''
    while finish >= start:
        if (finish - start) < step_user:
            step_user = finish - start + 1
        for i in range(min_number, max_number+1):
            for j in range(step_user):
                print(f'{start + j} x {i} = {(start + j) * i}', end='\t')
            print('\n', end='')
        print('\n', end='')
        start += step_user


def convert_number_to_number_system(number: int, system: int) -> str:
    '''
    Возвращает десятичное число в нужной системе счисления, максимальная система счисления - 36
    '''
    digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    if system > len(digits): return None
    result = ''
    while number > 0:
        result = digits[number % system] + result
        number //= system
    return result