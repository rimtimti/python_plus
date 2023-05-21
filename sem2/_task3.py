# Напишите программу, которая получает целое число и возвращает его двоичное, восьмеричное строковое представление.
# Функции bin и oct используйте для проверки своего результата, а не для решения.

# Дополнительно:
# Попробуйте избежать дублирования кода в преобразованиях к разным системам счисления
# Избегайте магических чисел
# Добавьте аннотацию типов где это возможно
import pyth

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

NUMBER = 42
SYSTEM_NUMBER = 18

print(convert_number_to_number_system(NUMBER, SYSTEM_NUMBER))
print(int(str(convert_number_to_number_system(NUMBER, SYSTEM_NUMBER)), SYSTEM_NUMBER))