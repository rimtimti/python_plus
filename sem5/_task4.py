# Создайте генератор чётных чисел от нуля до 100.
# ✔ Из последовательности исключите числа, сумма цифр которых равна 8.
# ✔ Решение в одну строку.

START = 0
FINISH = 100
PARITY = 2
SUM_EXCLUDING = 8


def gen_num() -> print:
    return [
        i for i in range(START, FINISH + 1, PARITY) if i // 10 + i % 10 != SUM_EXCLUDING
    ]


print(gen_num())
