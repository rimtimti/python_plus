# Создайте класс с базовым исключением и дочерние классы исключения:
# ○ ошибка уровня,
# ○ ошибка доступа.


class CustomException(Exception):
    pass


class LevelError(CustomException):
    def __init__(self, value: int):
        self.value = value

    def __str__(self):
        return f'ОТКАЗ ДОСТУПА. Ваш уровень ниже {self.value}'


class AccessError(CustomException):
    def __init__(self, User):
        self.user_id = User.user_id
        self.name = User.name

    def __str__(self):
        return f'Пользователь (ID = {self.user_id} Имя = {self.name}) в базе не найден.'
