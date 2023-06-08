# Самостоятельно сохраните в переменной строку текста.
# ✔ Создайте из строки словарь, где ключ — буква, а значение — код буквы.
# ✔ Напишите преобразование в одну строку.


def from_str_to_dict(text_2: str) -> dict[str:int]:
    return {k: ord(k) for k in text_2}


print(from_str_to_dict('sdsdsdddfgdfgdfgdfgasdgasgas'))
