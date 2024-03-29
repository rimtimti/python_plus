# Функция принимает на вход три списка одинаковой длины: имена str, ставка int, премия str с указанием процентов вида “10.25%”.
# Вернуть словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии


def calc_bonus(names: list[str], rates: list[int], bonus: list[str]) -> dict[str:float]:
    """
    Принимает принимает на вход три списка одинаковой длины. Возвращает словарь с именем в качестве ключа и суммой премии в качестве значения.
    """
    return {
        names: rates * bonus / 100
        for names, rates, bonus in zip(names, rates, (float(i[:-1]) for i in bonus))
    }


print(
    calc_bonus(
        ["Сергей", "Иван", "Артем"], [20000, 40000, 35000], ["10%", "7.5%", "5.5%"]
    )
)
