# Вспоминаем задачу из семинара 8 про сериализацию данных, где в бесконечном цикле запрашивали имя,
# личный идентификатор и уровень доступа (от 1 до 7) сохраняя информацию в JSON файл.
# Напишите класс пользователя, который хранит эти данные в свойствах экземпляра.
# Отдельно напишите функцию, которая считывает информацию из JSON файла и формирует множество пользователей.

# Доработаем задачи 3 и 4.
# Создайте класс проекта, который имеет следующие методы:
# загрузка данных (функция из задания 4)
# вход в систему - требует указать имя и id пользователя.
#   Для проверки наличия пользователя в множестве используйте магический метод проверки на равенство пользователей.
#   Если такого пользователя нет, вызывайте исключение доступа.
#   А если пользователь есть, получите его уровень из множества пользователей.
# добавление пользователя.
#   Если уровень пользователя меньше, чем ваш уровень, вызывайте исключение уровня доступа.

import json

import sys
sys.path.insert(1, '../python_plus')
import errors

FILE_NAME = 'sem13//data.json'


class User:

    def __init__(self, level: int, user_id: int, name: str):
        self.level = level
        self.user_id = user_id
        self.name = name

    def __eq__(self, other):
        return self.user_id == other.user_id and self.name == other.name

    def __str__(self):
        return f'\nУровень доступа = {self.level}. ID = {self.user_id}. Имя = {self.name}'


class Access:

    def __init__(self):
        data = self.read_json(FILE_NAME)
        user_list = self.parse_data(data)
        self.data = user_list

    def read_json(self, file_name: str) -> dict:
        with open(file_name, 'r', encoding='utf-8') as f:
            try:
                return json.load(f)
            except:
                return {}

    def parse_data(self, data: dict) -> list[User]:
        user_list = []
        for level, dict_users in data.items():
            for user_id, name in dict_users.items():
                user_list.append(User(int(level), int(user_id), name))
        return user_list

    def enter_system(self, enter_level: int, user_id: int, name: str):
        temp_user = User(0, user_id, name)
        if temp_user in self.data:
            for user in self.data:
                if temp_user == user:
                    temp_user.level = user.level
        else:
            raise errors.AccessError(temp_user)
        if enter_level <= temp_user.level:
            return f'ДОСТУП РАЗРЕШЕН: {temp_user}'
        else:
            raise errors.LevelError(enter_level)

if __name__ == '__main__':
    access = Access()
    # data = access.read_json(FILE_NAME)
    # # print(data)
    # print(*access.parse_data(data))
    # print(*access.data)
    print(access.enter_system(3, 4, "Артур"))
    print(access.enter_system(4, 4, "Артур"))
    print(access.enter_system(2, 6, "Иван"))
