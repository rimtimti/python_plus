# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.

def exchange_key_and_value(**kwargs):
    result = dict()
    for key, value in kwargs.items():
        if isinstance(value, (list, dict, set, bytearray)):
            value = str(value)
        result[value] = key
    return result


print(exchange_key_and_value(language='Python',
                             variable='x',
                             function=['set', 'zip', 'filter']))
