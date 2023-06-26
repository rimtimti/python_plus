# Решить задачи, которые не успели решить на семинаре.
# Добавьте ко всем задачам с семинара строки документации и методы вывода информации на печать.
# Создайте класс Матрица. Добавьте методы для:
# ○ вывода на печать,
# ○ сравнения,
# ○ сложения,
# ○ *умножения матриц


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
            result += f'{[i for i in item]}\n'
        return result

    def __eq__(self, other):
        '''
        Переопределённый метод для сравнения матриц.
        Матрицы могут быть равны когда равны их длины и каждый элемент
        '''
        return self.matrix == other.matrix

    def __add__(self, other):
        '''
        Переопределённый метод поэлементного сложения матриц.
        Можно складывать только матрицы одинаковой размерности
        '''
        if len(self.matrix) == len(other.matrix) and set(len(i) for i in self.matrix) == set(len(i) for i in other.matrix):
            result = [map(sum, zip(*i))
                      for i in zip(self.matrix, other.matrix)]
        else:
            result = [['Сложение'], ['этих матриц'], ['невозможно']]
        return Matrix(result)

    def __mul__(self, other):
        '''
        Переопределенный метод умножения матриц.
        Можно умножать матрицы при одинаковой длине строк в первой и столбцов во второй
        '''
        result = [[0]*len(other.matrix[0]) for _ in range(len(self.matrix))]
        for i in range(len(self.matrix)):
            for j in range(len(other.matrix[0])):
                for k in range(len(other.matrix)):
                    result[i][j] += self.matrix[i][k] * other.matrix[k][j]
# Решение через zip
        # result = [[sum(a * b for a, b in zip(Arow, Bcol)) for Bcol in zip(*other.matrix)] for Arow in self.matrix]
        return Matrix(result)


if __name__ == '__main__':
    matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    matrix_2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    sum_matrix = matrix_1 + matrix_2
    print(sum_matrix)
    matrix_3 = Matrix([[2, 2, 2], [2, 2, 2]])
    matrix_4 = Matrix([[3, 3], [3, 3], [3, 3]])
    mul_matrix = matrix_3 * matrix_4
    print(mul_matrix)
    print(matrix_1 == matrix_2)
