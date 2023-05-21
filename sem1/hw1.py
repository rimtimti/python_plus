# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c — стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

import defs

SIZE = 3

array = defs.get_array_float_number_required_size('Введите стороны треугольника через запятую: ', SIZE)
result = 'Этот треугольник '

for i in range(len(array)):
    if array[i] >= (sum(array) - array [i]):
        result += 'не существует.'
        break
else:
    match len(set(array)):
        case 1:
            result += 'равносторонний'
        case 2:
            result += 'равнобедренный'
        case 3:
            result += 'разносторонний'
print(result)