# Создайте функцию генератор чисел Фибоначчи (см. Википедию).

# Также реализуйте возможность запуска из командной строки с передачей параметров.

import argparse

def fibonacci(n: int) -> list[int]:
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


# print(*(fibonacci(15)))
parser = argparse.ArgumentParser(description="Проверка треугольника")
parser.add_argument("param", metavar="a b c", type=int, nargs=1, help="Введите a b c через пробел")
args = parser.parse_args()
print(*(fibonacci(*args.param)))
