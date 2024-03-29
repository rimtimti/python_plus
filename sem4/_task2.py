# Напишите функцию, которая принимает строку текста.
# Сформируйте список с уникальными кодами Unicode каждого символа введённой строки отсортированный по убыванию


def unicode_sort(text: str) -> list[int]:
    """
    Принимает текст и выдает список с уникальными кодами Unicode каждого символа введённой строки отсортированный по убыванию
    """
    # result = set()
    # for symbol in text:
    #     result.add(ord(symbol))
    # return sorted(result, reverse=True)
    return sorted(set([ord(symbol) for symbol in text]), reverse=True)


print(unicode_sort("Python является мультипарадигменным языком программирования"))
