# Создайте вручную список с повторяющимися целыми числами.
# Сформируйте список с порядковыми номерами нечётных элементов исходного списка.
# Нумерация начинается с единицы

def get_numbers_odd_elements_of_the_original_list(array: list) -> list:
    '''
    Получает массив и выдает порядковые номера нечётных элементов исходного списка
    '''
    # result = []
    # for i, elem in enumerate(array, start=1):
    #     if elem % 2:
    #        result.append(i)
    # return result
    return [i for i, j in filter(lambda x: x[1] % 2 != 0, enumerate(array, 1))]


arr = [22, 23, 13, 23, 22, 25, 16, 46, 25, 13]
print(get_numbers_odd_elements_of_the_original_list(arr))
