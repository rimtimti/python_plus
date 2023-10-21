# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.
# ✔ Таблицу создайте в виде однострочного генератора, где каждый элемент генератора — отдельный пример таблицы умножения.
# ✔ Для вывода результата используйте «принт» без перехода на новую строку.


def mult_table():
    LOWER_LIMIT = 2
    UPPER_lIMIT = 10
    COLUMN = 4
    print(" ", end="")
    print(
        *(
            f"{k:>} x {j:>2} = {k * j:>2}\n\n"
            if j == UPPER_lIMIT and k == i + COLUMN - 1
            else f"{k:>} x {j:>2} = {k * j:>2}\n"
            if k == i + COLUMN - 1
            else f"{k:>} x {j:>2} = {k * j:>2}\t\t"
            for i in range(LOWER_LIMIT, UPPER_lIMIT, COLUMN)
            for j in range(LOWER_LIMIT, UPPER_lIMIT + 1)
            for k in range(i, i + COLUMN)
        )
    )


mult_table()
