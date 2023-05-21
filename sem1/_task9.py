# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.
import defs

START = 2
FINISH = 9
MIN_NUMBER = 2
MAX_NUMBER = 10
STEP = 4

print('\n\t\t    ТАБЛИЦА УМНОЖЕНИЯ\n')
defs.view_table_multiplication(START, FINISH, MIN_NUMBER, MAX_NUMBER, STEP)
