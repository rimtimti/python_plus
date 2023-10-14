# Пользователь вводит строку текста.
# Подсчитайте сколько раз встречается каждая буква в строке без использования метода count и с ним.
# Результат сохраните в словаре, где ключ — символ, а значение — частота встречи символа в строке.
# Обратите внимание на порядок ключей.
# Объясните почему они совпадают или не совпадают в ваших решениях.


def task_7_hard(text) -> tuple:
    """
    Просит у пользователя текст, выдает сколько раз встречается каждая буква в строке
    """
    input_data = input(text)
    result = {}
    for i in input_data:
        count = 0
        for j in input_data:
            if i not in result and i == j:
                count += 1
        result.setdefault(i, count)
    return result


def task_7_simple(text) -> tuple:
    """
    Просит у пользователя текст, выдает сколько раз встречается каждая буква в строке
    """
    input_data = input(text)
    return {i: input_data.count(i) for i in input_data if i}


text = "Введите текст: "
print(task_7_hard(text))
print(task_7_simple(text))
