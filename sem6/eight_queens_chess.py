# Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

# Напишите функцию в шахматный модуль.
# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различный случайные варианты и выведите 4 успешных расстановки.

import random
START = 1
FINISH = 8


def check_eight_queens(queens: list[(int, int)]) -> bool:
    if len(queens) != FINISH:
        return f'Неверный ввод числа ферзей на доске.'
    x = list(i[0] for i in queens)
    y = list(i[1] for i in queens)

    for i in range(len(queens)):
        for j in range(i + 1, len(queens)):
            if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
                return False
    return True


def _generate_random_queens_coordinates() -> list[(int, int)]:
    coordinates = []
    i = 0
    while i < FINISH:
        x, y = random.randint(START, FINISH), random.randint(START, FINISH)
        if x not in list(i[0] for i in coordinates) and (x, y) not in set(coordinates):
            coordinates.append((x, y))
            i += 1
    return sorted(coordinates)


def show_unique_solutions(combination: int) -> print:
    solutions = []
    count = 0
    while count < combination:
        temp = _generate_random_queens_coordinates()
        if check_eight_queens(temp) and temp not in solutions:
            print(temp)
            solutions.append(temp)
            count += 1
