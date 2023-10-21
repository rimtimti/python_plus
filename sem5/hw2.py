# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида «10.25%».
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения
# Сумма рассчитывается как ставка умноженная на процент премии


names = ["Сидоров", "Иванов", "Петров", "Захаров"]
salary = [200_000, 300_000, 150_000, 250_000]
bonus = ["10.25%", "15.00%", "18.50%", "12.05%"]


def get_bonus(names: list[str], salary: list[int], bonus: list[str]) -> dict[str:float]:
    return {
        name: (sale * bonus / 100)
        for name, sale, bonus in zip(names, salary, (float(i[:-1]) for i in bonus))
    }.items()


print(*(get_bonus(names, salary, bonus)))
