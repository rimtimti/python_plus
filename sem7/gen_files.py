# Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.
from random import randint, choice
from pathlib import Path
import os

A = 97
Z = 122


def gen_files(directory: Path, extension: str, min_len_name: int = 6, max_len_name: int = 30, min_len_byte: int = 256,
              max_len_byte: int = 4096, count_files: int = 42) -> None:
    if os.path.isdir(directory) == False:
        os.mkdir(directory)
    os.chdir(directory)
    for _ in range(count_files):
        rad_string = ''.join(chr(randint(A, Z)) for _ in range(randint(min_len_name, max_len_name)))
        data = bytes(randint(0, 255) for _ in range(randint(min_len_byte, max_len_byte)))
        with open(f'{rad_string}.{extension}', 'wb') as f:
            f.write(data)