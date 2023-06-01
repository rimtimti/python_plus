# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.


def get_duplicate_elements(array: list[int]) -> list[int]:
    '''
    Выдает список повторяющихся элементов списка
    '''
    return [i for i in set(array) if array.count(i) > 1]


arr = [22, 23, 13, 23, 22, 25, 16, 46, 25, 13]
print(get_duplicate_elements(arr))
