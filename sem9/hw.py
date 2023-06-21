# Решить задачи, которые не успели решить на семинаре.
# Напишите следующие функции:
# ○ Нахождение корней квадратного уравнения
# ○ Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# ○ Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# ○ Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
# Соберите пакет с играми из тех файлов, что уже были созданы в рамках курса
import csv
import json
import random
from typing import Callable

ACCURACY = 14
COUNT_NUMBERS = 3
MIN_NUMBER = -100
MAX_NUMBER = 100
MIN_COUNT_STRING_CSV = 100
MAX_COUNT_STRING_CSV = 1000
FILE_CSV = 'numbers.csv'
FILE_JSON = 'result.json'
ABC = ['a', 'b', 'c']


def deco_in_csv(file: str) -> object:
    def deco(func: Callable):
        def wrapper(*args, **kwargs):
            result = {}
            with open(file, 'r') as f:
                reader = csv.reader(f, dialect='excel')
                count = 0
                item = {}
                for row in reader:
                    if count > 0:
                        ABC.append('result')
                        row.append(func(row))
                        item = {count: dict(zip(ABC, row))}
                    result.update(item)
                    count += 1
            return result
        return wrapper
    return deco


def write_to_json(file: str):
    def deco(func: Callable):
        def wrapper(*args, **kwargs):
            result = func()
            with open(file, 'w', encoding='utf-8') as f:
                json.dump(result, f, indent=2, ensure_ascii=False)

        return wrapper
    return deco


@write_to_json(FILE_JSON)
@deco_in_csv(FILE_CSV)
def solve_quadratic_item(array: list) -> tuple[str, str] | str:
    '''
    Решает уравнение вида a*x² + b*x + c = 0
    '''
    a, b, c = [int(i) for i in array]
    discriminant = round(b ** 2 - 4 * a * c, ACCURACY)
    if a == 0 and b == 0:
        return None
    elif a == 0:
        x1 = -(c / b)
        return str(x1)
    else:
        x1 = (-b + discriminant ** 0.5) / (2 * a)
        x2 = (-b - discriminant ** 0.5) / (2 * a)
    if discriminant < 0:
        x1 = complex(round(x1.real, ACCURACY), round(x1.imag, ACCURACY))
        x2 = complex(round(x2.real, ACCURACY), round(x2.imag, ACCURACY))
    if discriminant != 0:
        return str(x1), str(x2)
    else:
        return str(x1)


def generate_count_numbers() -> list[int]:
    return [random.randint(MIN_NUMBER, MAX_NUMBER) for _ in range(COUNT_NUMBERS)]


def write_to_csv(file: str) -> None:
    list_csv = []
    for _ in range(random.randint(MIN_COUNT_STRING_CSV, MAX_COUNT_STRING_CSV)):
        list_csv.append(generate_count_numbers())
    with open(file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(ABC)
        writer.writerows(list_csv)


if __name__ == '__main__':
    write_to_csv(FILE_CSV)
    solve_quadratic_item()
