# Создайте генератор чётных чисел от нуля до 100.
# ✔ Из последовательности исключите числа, сумма цифр которых равна 8.
# ✔ Решение в одну строку.


def gen_num() -> print:
    return [i for i in range(0, 101, 2) if i // 10 + i % 10 != 8]


print(gen_num())