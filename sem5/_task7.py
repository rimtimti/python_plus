# Создайте функцию-генератор.
# ✔ Функция генерирует N простых чисел, начиная с числа 2.
# ✔ Для проверки числа на простоту используйте правило: «число является простым, если делится нацело только на единицу и на себя».

FINISH = 45


def simple_numbers(finish: int):
    """
    Выдает простые числа от 2 и до finish по одному
    """
    for i in range(2, finish + 1):
        simple = True
        for j in range(2, i - 1):
            if not i % j:
                simple = False
        if simple:
            yield i


print(*simple_numbers(FINISH))
