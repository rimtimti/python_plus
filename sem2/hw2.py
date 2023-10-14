# Напишите программу, которая принимает две строки вида “a/b” — дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение дробей.
# Для проверки своего кода используйте модуль fractions.
# Сделал все 4 математических действия

import fractions
import math


def get_str_fraction(text: str) -> list[int]:
    """
    Просит у пользователя ввести дробь вида a/b, проверяет ввод, сокращает дробь
    """
    try:
        array = input(text).strip().split("/")
        if int(array[1]) == 0 or int(array[0]) == 0:
            print("Знаменатель или числитель дроби не должен быть равен 0 !!!")
            return get_str_fraction(text)
        elif len(array) == 2:
            if all(map(lambda x: int(x), array)):
                array = [int(x) for x in array]
                return cut_fraction(array)
        else:
            print("Неверный ввод!!!")
            return get_str_fraction(text)
    except ValueError:
        print("Неверный ввод!!!")
        return get_str_fraction(text)


def cut_fraction(array: list[int, int]) -> list[int, int]:
    """
    Сокращает числа на наибольший общий делитель, если он есть
    """
    if math.gcd(array[0], array[1]):
        return [int(x / math.gcd(array[0], array[1])) for x in array]
    else:
        return array


def get_sign(text: str) -> str:
    """
    Просит у пользователя ввести математический знак, проверяет ввод, возвращает его
    """
    try:
        sign = input(text)
        if sign in "+-*/":
            return sign
        else:
            print("Неверный ввод!!!")
            return get_sign(text)
    except ValueError:
        print("Неверный ввод!!!")
        return get_sign(text)


def sum_fraction(array_1: list[int, int], array_2: list[int, int]) -> list[int, int]:
    """
    Складывает 2 простые дроби, сокращает результат
    """
    result = [
        array_1[0] * array_2[1] + array_2[0] * array_1[1],
        array_1[1] * array_2[1],
    ]
    return cut_fraction(result)


def multypl_fraction(
    array_1: list[int, int], array_2: list[int, int]
) -> list[int, int]:
    """
    Перемножает 2 простые дроби, сокращает результат
    """
    result = [array_1[0] * array_2[0], array_1[1] * array_2[1]]
    return cut_fraction(result)


def print_fraction(array: list[int, int]) -> print:
    """
    Печатает простую дробь
    """
    return array[0] if array[1] == 1 else f"{array[0]}/{array[1]}"


def print_answer(
    array_1: list[int, int], array_2: list[int, int], symbol: str, operation
) -> print:
    """
    Выводит на экран пример с двумя дробями и результат операции
    """
    print(
        f"{print_fraction(array_1)} {symbol} {print_fraction(array_2)} = {print_fraction(operation)}"
    )


def run():
    print(
        "Программа просит ввести 2 дроби вида a/b и математический знак. Затем выводит результат вычисления двумя способами."
    )
    arr_1 = get_str_fraction("Введите первую дробь вида a/b: ")
    sign = get_sign("Введите математический знак ( +, -, *, / ): ")
    arr_2 = get_str_fraction("Введите вторую дробь вида a/b: ")
    f1 = fractions.Fraction(arr_1[0], arr_1[1])
    f2 = fractions.Fraction(arr_2[0], arr_2[1])
    match sign:
        case "+":
            result = sum_fraction(arr_1, arr_2)
            result_fraction = f1 + f2
        case "-":
            result_fraction = f1 - f2
            arr_2[0] *= -1
            result = sum_fraction(arr_1, arr_2)
            arr_2[0] *= -1
        case "*":
            result = multypl_fraction(arr_1, arr_2)
            result_fraction = f1 * f2
        case "/":
            result = multypl_fraction(arr_1, arr_2[::-1])
            result_fraction = f1 / f2
    return print_answer(arr_1, arr_2, sign, result), print(
        "Проверка с помощью fractions:", result_fraction
    )


run()
