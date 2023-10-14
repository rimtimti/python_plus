# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.
import itertools

things = {"bottle": 3, "tent": 3, "travel mat": 3, "spare shoes": 3, "map": 3}


# def goes_into_backpack(capacity: int, things: dict) -> list[str]:
#     """
#     Возвращает 1 вариант
#     """
#     things = dict(sorted(things.items(), key=lambda item: -item[1]))
#     packaging_option = []
#     for key, value in things.items():
#         if value <= capacity:
#             capacity -= value
#             packaging_option.append(key)
#     return packaging_option


# print(goes_into_backpack(15, things))


def goes_into_backpack2(capacity: int, things: dict) -> list[(tuple)]:
    """
    Возвращает все варианты
    """
    data = []
    result = []
    for i in range(1, len(things) + 1):
        data += itertools.combinations(things.keys(), i)
    for i in data:
        weight = 0
        for j in i:
            if j in things:
                weight += things.get(j)
        if weight == capacity:
            result.append(i)
    return result


print(goes_into_backpack2(9, things))
