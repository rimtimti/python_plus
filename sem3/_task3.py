# Создайте вручную кортеж содержащий элементы разных типов.
# Получите из него словарь списков, где ключ - тип элемента, значение - список элементов данного типа

def task_3(tuple_in: tuple) -> dict:
    '''
    Получает кортеж и выдает словарь списков, где ключ - тип элемента, значение - список элементов данного типа
    '''
    result = {}
    for i in tuple_in:
        result.setdefault(type(i), []).append(i)
    return result


tuple_in = (8, "asd", 156, True, False, True, 0, "ррпро", 5.45151)
print(task_3(tuple_in))
