# Решить задачи, которые не успели решить на семинаре.
# Добавьте ко всем задачам с семинара строки документации и методы вывода информации на печать.
# Создайте класс Матрица. Добавьте методы для:
# ○ вывода на печать,
# ○ сравнения,
# ○ сложения,
# ○ *умножения матриц

import sys
sys.path.insert(1, '../python_plus')

# Добавьте логирование ошибок и полезной информации.

import logging

logging.basicConfig(style="{", filename='matrix_info.log',
                    level=logging.INFO, encoding="UTF-8")

logger = logging.getLogger(__name__)

class Matrix:
    '''
    Класс матрица с инициализацией списка списков, с переопределенными методами сравнения, сложения, умножения и строчного вывода
    '''

    def __init__(self, matrix: list[list[int]]):
        '''
        Инициализация класса
        '''
        self.matrix = matrix

    def __str__(self):
        '''
        Вывод списка списков
        '''
        result = ''
        for item in self.matrix:
            result += f'{[i for i in item]}'
        return result

    def __eq__(self, other):
        '''
        Переопределённый метод для сравнения матриц.
        Матрицы могут быть равны когда равны их длины и каждый элемент
        '''
        self = self.matrix_exist()
        other = other.matrix_exist()
        if self.matrix == other.matrix:
            logger.info(f'Матрицы: {self.matrix} и {other.matrix} - равны')
        else:
            logger.info(f'Матрицы: {self.matrix} и {other.matrix} - не равны')


    def __add__(self, other):
        '''
        Переопределённый метод поэлементного сложения матриц.
        Можно складывать только матрицы одинаковой размерности.
        '''
        self = self.matrix_exist()
        other = other.matrix_exist()
        if len(self.matrix) == len(other.matrix) and set(len(i) for i in self.matrix) == set(len(i) for i in other.matrix):
            result = [map(sum, zip(*i))
                      for i in zip(self.matrix, other.matrix)]
            logger.info(f'Матрицы: {self.matrix} и {other.matrix} - можно сложить. Результат = {Matrix(result)}')
        else:
            logger.error(f'Матрицы нельзя сложить: {self.matrix} и {other.matrix}')


    def __mul__(self, other):
        '''
        Переопределенный метод умножения матриц.
        Можно умножать матрицы при одинаковой длине строк в первой и столбцов во второй.
        '''
        self = self.matrix_exist()
        other = other.matrix_exist()
        if len(other.matrix) == len(self.matrix[0]):           
            result = [[0]*len(other.matrix[0]) for _ in range(len(self.matrix))]
            for i in range(len(self.matrix)):
                for j in range(len(other.matrix[0])):
                    for k in range(len(other.matrix)):
                        result[i][j] += self.matrix[i][k] * other.matrix[k][j]
            logger.info(f'Матрицы: {self.matrix} и {other.matrix} - можно перемножить. Результат = {Matrix(result)}')
        else:
            logger.error(f'Матрицы нельзя перемножить: {self.matrix} и {other.matrix}')
# Решение через zip
        # result = [[sum(a * b for a, b in zip(Arow, Bcol)) for Bcol in zip(*other.matrix)] for Arow in self.matrix]


    def matrix_exist(self):
        if len(set([len(item) for item in self.matrix])) != 1:
            logger.error(f'Матрица {self.matrix} содержит пустые значения')
        elif None in set([j for i in [*self.matrix] for j in i]):
            logger.error(f'Матрица {self.matrix} содержит None')
        else:
            logger.info(f'Матрица {self.matrix} корректна')
            return Matrix(self.matrix)


if __name__ == '__main__':
    matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    matrix_2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    matrix_3 = Matrix([[2, 2, 2], [2, 2, 2]])
    matrix_4 = Matrix([[3, 3], [3, 3], [3, 3]])

    print(matrix_1 + matrix_2)
    print(matrix_1 + matrix_4)
    print(matrix_3 * matrix_4)
    print(matrix_4 * matrix_2)
    print(matrix_1 == matrix_2)
    print(matrix_3 + matrix_4)
    print(matrix_3 == matrix_2)
    