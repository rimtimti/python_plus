# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.
import itertools
things = {'bottle': 2, 'tent': 8, 'travel mat': 3, 'spare shoes': 4, 'map': 1}


def goes_into_backpack(capacity: int, things: dict) -> list[str]:
    things = dict(sorted(things.items(), key=lambda item: -item[1]))
    packaging_option = []
    for key, value in things.items():
        if value <= capacity:
            capacity -= value
            packaging_option.append(key)
    return packaging_option


print(goes_into_backpack(15, things))
