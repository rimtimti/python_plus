# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.

from datetime import datetime

__all__ = ["check_year", "date_validator"]
MIN_YEAR = 1
MAX_YEAR = 10_000


def _check_leap_year(date: str) -> bool:
    CHECK_LEAP_YEAR_1 = 4
    CHECK_LEAP_YEAR_2 = 100
    year = int(date.split(".")[-1])
    return (
        year in range(MIN_YEAR, MAX_YEAR)
        and year % CHECK_LEAP_YEAR_1 == 0
        and year % CHECK_LEAP_YEAR_2 != 0
        or year % (CHECK_LEAP_YEAR_2 * CHECK_LEAP_YEAR_1) == 0
    )


def check_year(year: str) -> bool:
    try:
        datetime.strptime(year, "%d.%m.%Y").date()
        return True
    except:
        return False


def date_validator(date: str) -> str:
    if check_year(date):
        return (
            f"Этот год високосный"
            if _check_leap_year(date)
            else f"Это не високосный год"
        )
    else:
        return f"Дата введена некорректно"
