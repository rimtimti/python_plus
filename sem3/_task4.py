# Создайте вручную список с повторяющимися элементами.
# Удалите из него все элементы, которые встречаются дважды.


def task_4(array: list[int]) -> list[int]:
    """
    Получает массив и удаляет из него все элементы, которые встречаются дважды
    """
    # for item in set(array):
    #     count = array.count(item)
    #     if count > 1:
    #         for _ in range(count):
    #             array.remove(item)
    # return array
    return list(filter(lambda x: array.count(x) != 2, array))


arr = [22, 23, 13, 23, 22, 25, 16, 46, 25, 13]
print(task_4(arr))
