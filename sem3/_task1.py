# Вручную создайте список с целыми числами, которые повторяются.
# Получите новый список, который содержит уникальные (без повтора) элементы исходного списка.
# *Подготовьте два решения, короткое и длинное, которое не использует другие коллекции помимо списков


def get_uniq_elements_1(array: list[int]) -> list[int]:
    """
    Выдает уникальные элементы списка (длинное решение)
    """
    res = []
    for i in range(len(array)):
        if array[i] not in res:
            res.append(array[i])
    return sorted(res)


def get_uniq_elements_2(array: list[int]) -> list[int]:
    """
    Выдает уникальные элементы списка (коротрое решение)
    """
    return sorted(list(set(array)))


arr = [22, 23, 13, 23, 22, 25, 16, 46, 25, 13]

print(get_uniq_elements_1(arr))
print(get_uniq_elements_2(arr))
