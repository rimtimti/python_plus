# Создайте класс с базовым исключением и дочерние классы исключения:
# ○ ошибка уровня,
# ○ ошибка доступа.


class CustomException(Exception):
    pass


class MatrixExistsError(CustomException):
    def __init__(self, matrix: list[list[int]]):
        self.matrix = matrix

    def __str__(self):
        return f'{self.matrix} - это не матрица !'


class MatrixNoneError(CustomException):
    def __init__(self, matrix: list[list[int]]):
        self.matrix = matrix

    def __str__(self):
        return f'{self.matrix}Матрица содержит None !'


class MatricesDifferentSizeError(CustomException):
    def __init__(self, matrix1: list[list[int]], matrix2: list[list[int]]):
        self.matrix1 = matrix1
        self.matrix2 = matrix2

    def __str__(self):
        return f'\n{self.matrix1}\n{self.matrix2}\nМатрицы разного размера нельзя складывать !\n'\
            f'Можно складывать только матрицы одинаковой размерности.'


class MatrixMultiplicationError(CustomException):
    def __init__(self, matrix1: list[list[int]], matrix2: list[list[int]]):
        self.matrix1 = matrix1
        self.matrix2 = matrix2

    def __str__(self):
        return f'\n{self.matrix1}\n{self.matrix2}\nМатрицы такого размера нельзя переморжать !\n'\
            f'Можно умножать матрицы при одинаковой длине строк в первой и столбцов во второй.'
