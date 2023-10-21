# Пользователь вводит строку из четырёх или более целых чисел, разделённых символом “/”.
# Сформируйте словарь, где:
# ✔второе и третье число являются ключами.
# ✔первое число является значением для первого ключа.
# ✔четвертое и все возможные последующие хранятся в кортеже как значения второго ключа.

text = "9/15/67/1/19/6/3"


def task_1(text: str) -> dict[int:int]:
    first, second, third, *other = (int(i) for i in text.split("/"))
    return {second: first, third: tuple(other)}


print(task_1(text))
