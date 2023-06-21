# Напишите декоратор, который сохраняет в json файл параметры декорируемой функции и результат, который она возвращает.
# При повторном вызове файл должен расширяться, а не перезаписываться.
# Каждый ключевой параметр сохраните как отдельный ключ json словаря.
# Для декорирования напишите функцию, которая может принимать как позиционные, так и ключевые аргументы.
# Имя файла должно совпадать с именем декорируемой функции.
import json
from typing import Callable
from pathlib import Path


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


if __name__ == '__main__':
    multy(2, 5)
    multy(3, 5)
    multy(36, 55)
    multy(36, 554)