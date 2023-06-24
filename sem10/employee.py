# Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания.
# У сотрудника должен быть:
# ○ шестизначный идентификационный номер
# ○ уровень доступа вычисляемый как остаток от деления суммы цифр id на семь

import random

from human import Human

MIN_NUM = 100000
MAX_NUM = 999999
LEVEL_NUM = 7

# ТУТ я решил по-другому, на семинаре получилось у вас так, что код - дробное число, а так быть не должно

class Employee(Human):

    def __init__(self, profession: str, firstname: str, lastname: str, age: int, gender: str):
        super().__init__(firstname, lastname, age, gender)
        self.eml_id = random.randint(MIN_NUM, MAX_NUM)
        self.sec_level = self._secure_level()
        self.profession = profession

    def _secure_level(self):
        return sum([int(i) for i in str(self.eml_id)]) % LEVEL_NUM

    def __str__(self):
        return f'{self.eml_id} {self.sec_level} {self.firstname} {self.lastname} {self.get_age()} {self.gender} {self.profession}'


if __name__ == '__main__':
    eml_1 = Employee('Рабочий', 'Иван', 'Иванов', 25, 'мужской')
    print(eml_1)
