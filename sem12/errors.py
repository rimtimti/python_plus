# Создайте класс с базовым исключением и дочерние классы исключения:
# ○ ошибка уровня,
# ○ ошибка доступа.


class CustomException(Exception):
    pass

class PositiveValueError(CustomException):
    def __init__(self, value: int):
        self.value = value

    def __str__(self):
        return f'Значение должно быть положительное, а не {self.value} !'
