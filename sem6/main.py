from sys import argv
from puzzle_numbers import gen_fnc
from puzzle_mystery import puzzle
from puzzle_mistery_with_dict import new_puzzle, show_statistic
from leap_year import date_validator
from eight_queens_chess import check_eight_queens, show_unique_solutions


if __name__ == "__main__":
    # gen_fnc(*[int(i) for i in argv[1:]])
    # print(puzzle("Зимой и летом одним цветом", ["eль", "ёлка", "Елка", "Ель"], 3))
    # puzzle_dict = {
    #     "Зимой и летом одним цветом": ["eль", "ёлка", "Елка", "Ель"],
    #     "Красна девица, а коса на улице": ["морковь", "морковка"],
    #     "Два кольца, два конца, в по середине гвоздик": ["ножницы"],
    # }
    # print(new_puzzle(puzzle_dict, 3))
    # show_statistic()

    # print(date_validator("15.12.1996"))
    # print(date_validator("28.05.1995"))
    # print(date_validator("02.12.1600"))
    # print(date_validator("02.12.2100"))
    # print(date_validator(argv[1]))

    # queens_1 = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)]
    # queens_2 = [(1, 4), (2, 2), (3, 8), (4, 5), (5, 7), (6, 1), (7, 3), (8, 6)]
    # queens_3 = [(1, 7), (2, 4), (3, 2), (4, 8), (5, 6), (6, 1), (7, 3), (8, 5)]
    # queens_4 = [(1, 6), (2, 2), (3, 7), (4, 1), (5, 4), (6, 8), (7, 5), (8, 3)]
    # print(check_eight_queens(queens_1))
    # print(check_eight_queens(queens_2))
    # print(check_eight_queens(queens_3))
    # print(check_eight_queens(queens_4))

    show_unique_solutions(4)
