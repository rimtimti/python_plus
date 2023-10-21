# Продолжаем развивать задачу 2.
# ✔ Возьмите словарь, который вы получили.
# Сохраните его итератор.
# ✔ Далее выведите первые 5 пар ключ-значение,
# обращаясь к итератору, а не к словарю.

COUNT = 5


def from_str_to_dict_2(text: str) -> dict[str:int]:
    res_iter = iter({k: ord(k) for k in text}.items())
    for _ in range(COUNT):
        print(next(res_iter))


from_str_to_dict_2("sdsdsddfghjkl;zxcvbnm,")
