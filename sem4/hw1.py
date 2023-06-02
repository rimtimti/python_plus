# Напишите функцию для транспонирования матрицы

def transpose_matrix(*array: list[int]) -> list[()] | str:
    '''
    Транспонирует матрицу, если это возможно
    '''
    if len(set(len(i) for i in list(array))) == 1:
        return list(zip(*array))
    else:
        return 'Эту матрицу нельзя транспонировать'


print(transpose_matrix([1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 9],
                       [10, 11, 12]))
