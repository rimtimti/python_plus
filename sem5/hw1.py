# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.


def split_path(text_path: str) -> tuple():
    return text_path[: text_path.rindex("\\") + 1], *text_path[
        text_path.rindex("\\") + 1 :
    ].split(".")


text_path = r"C:\Users\rimtimti\Desktop\Python_plus\sem1.py"
print(split_path(text_path))
