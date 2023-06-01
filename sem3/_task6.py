# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# Строки нумеруются начиная с единицы
# Слова выводятся отсортированными согласно кодировки Unicode
# Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки


def task_6() -> print:
    input_data = input("Введите текст: ")
    result = sorted(input_data.split())

    for i, word in enumerate(result, 1):
        print(f"{i} {word:>{len(max(result, key=len))}}")


task_6()
