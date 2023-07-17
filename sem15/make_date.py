# Функция получает на вход текст вида: “1-й четверг ноября”, “3-я среда мая” и т.п.
# Преобразуйте его в дату в текущем году.
# Логируйте ошибки, если текст не соответсвует формату.

import logging
from datetime import datetime
from calendar import monthrange

logging.basicConfig(style="{", filename='info.log',
                    level=logging.INFO, encoding="UTF-8")

logger = logging.getLogger(__name__)


def parse_str(text: str):
    week, day, month, *_ = text.split()
    try:
        week = int(week.split('-')[0])
        day = parse_day(day)
        month = parse_month(month)
        year = datetime.now().year
        if month == None:
            logger.error(f'Ошибка в названии месяца: {text.split()[2]}')
        else:
            days_count = monthrange(year, month)[1]
            week_counter = 0
            for i in range(1, days_count + 1):
                data = datetime(day=i, month=month, year=year)
                if data.weekday() == day:
                    week_counter += 1
                    if week_counter == week:
                        logger.info(f'\t{text}\t=\t{data.date()}  ')
                        return data.date()
                    else:
                        logger.error(
                            f'Ошибка: {week} {text.split()[1]} в этом месяце не существует')
                        break
    except:
        logger.error(f'Ошибка в номере недели: {week}')


def parse_month(month: str) -> int:
    months = {'янв': 1, 'фев': 2, 'мар': 3, "апр": 4, "мая": 5, "июн": 6,
              "июл": 7, "авг": 8, "сен": 9, "окт": 10, "ноя": 11, "дек": 12}
    return months.get(month[:3])


def parse_day(day: str) -> int:
    match day.lower():
        case "понедельник":
            return 0
        case "вторник":
            return 1
        case "среда":
            return 2
        case "четверг":
            return 3
        case "пятница":
            return 4
        case "суббота":
            return 5
        case "воскресенье":
            return 6
        case _:
            logger.error(f'Ошибка в названии дня недели: {day}')


if __name__ == '__main__':
    print(parse_str("11-й четверг ноября"))
    print(parse_str("3-я dсреда мая"))
    print(parse_str("f5-й понедельник июля"))
    print(parse_str("1-й понедельник tиюля"))
    print(parse_str("11-й четверг но ября"))
