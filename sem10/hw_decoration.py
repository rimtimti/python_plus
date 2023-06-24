import csv
import json
from pathlib import Path
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


class Decoration:
    COUNTER_COUNT = 5

    def deco(func: Callable):
        MAX_COUNT = 10
        MAX_NUM = 100
        MIN_COUNT = 1
        MIN_NUM = 1

        def wrapper(*args, **kwargs):
            input_count, input_num = args
            if MIN_COUNT > input_count or input_count > MAX_COUNT:
                input_count = random.randint(MIN_COUNT, MAX_COUNT)
            if MIN_NUM > input_num or input_num > MAX_NUM:
                input_num = random.randint(MIN_NUM, MAX_NUM)
            return func(input_count, input_num)

        return wrapper

    @deco
    def two_numbers(count_try: int, num: int) -> Callable[[], None]:
        def random_numbers():
            for i in range(1, count_try + 1):
                user_input = input(
                    'Введите число для отгадывания от 1 до 100: ')
                if int(user_input) == num:
                    print(f'Вы угадали с {i} попытки')
                    break
            else:
                print(f'Вы не угадали')

        return random_numbers

    def counter(param: int):
        def deco(func: Callable):
            my_list = []

            def wrapper(*args, **kwargs):
                for i in range(param):
                    result = func(*args, **kwargs)
                    my_list.append(result)
                return my_list

            return wrapper

        return deco

    @counter(COUNTER_COUNT)
    def fact(num: int) -> int:
        res = 1
        for i in range(2, num + 1):
            res *= i
        return res


    def deco_json(func: Callable):
        filename = Path(f'{func.__name__}.json')
        filename.touch(exist_ok=True)
        with open(filename, 'r') as f:
            try:
                dict_result = json.load(f)
            except:
                dict_result = {}

        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            dict_result.update({str(res): args})
            dict_result.update({**kwargs})
            with open(f'{func.__name__}.json', 'w') as f:
                json.dump(dict_result, f, indent=2)

        return wrapper

    @deco_json
    def multy(a: int, b: int, *args, **kwargs) -> int:
        return a * b

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
            list_csv.append(Decoration.generate_count_numbers())
        with open(file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(ABC)
            writer.writerows(list_csv)


if __name__ == '__main__':
    # print(Decoration.fact(5))
    # Decoration.two_numbers(30, 20)()
    # Decoration.write_to_csv(FILE_CSV)
    # Decoration.solve_quadratic_item()
    Decoration.multy(3, 5)
    Decoration.multy(36, 55)