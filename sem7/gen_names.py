# Напишите функцию, которая генерирует псевдоимена.
# Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых обязательно должны быть гласные.
# Полученные имена сохраните в файл.

from pathlib import Path
from random import randint, choice

VOWES = 'aeiouy'
A = 97
Z = 122


def name_gen(count: int, str_len_min: int, str_len_max: int, file: Path) -> None:
    with open(file, 'a', encoding='utf-8') as f:
        while count > 0:
            rand_string = ''.join(chr(randint(A, Z)) for _ in range(randint(str_len_min, str_len_max)))
            if set(rand_string).isdisjoint(VOWES) == False:
                f.write(f'{rand_string.capitalize()}\n')
                count -= 1
