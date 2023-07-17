# На семинаре про декораторы был создан логирующий декоратор.
# Он сохранял аргументы функции и результат её работы в файл.
# Напишите аналогичный декоратор, но внутри используйте модуль logging.

# Доработаем задачу 2.
# Сохраняйте в лог файл раздельно:
# ○ уровень логирования,
# ○ дату события,
# ○ имя функции (не декоратора),
# ○ аргументы вызова,
# ○ результат.


import logging
from typing import Callable

FORMAT = "{levelname} - {asctime}: {msg}"
logging.basicConfig(format=FORMAT, style="{", filename='info.log', level=logging.INFO, encoding="UTF-8")

logger = logging.getLogger(__name__)


def deco_logger(func: Callable):
    def wrapper(*args):
        a, b = args
        logger.info(f"{func.__name__} {a} * {b} = {func(a, b)}  ")

    return wrapper


@deco_logger
def multy(a: int, b: int) -> int:
    return a * b


if __name__ == '__main__':
    multy(2, 5)