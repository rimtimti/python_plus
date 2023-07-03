# Создайте класс студента.
# ○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# ○ Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
# ○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# ○ Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.
import csv
from statistics import mean

FILE_NAME = 'sem12//subjects.csv'
MIN_GRADE = 2
MAX_GRADE = 5
MIN_SCORE = 0
MAX_SCORE = 100
MEAN_ACCURACY = 2


class NameValidator:
    
    def __set_name__(self, _, name):
        self.private_name = '_' + name

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        self._name_validate(value)
        setattr(obj, self.private_name, value)

    def _name_validate(self, value):
        if not isinstance(value, str):
            raise AttributeError('Имя или фамилия не строка')
        if not value.isalpha():
            raise AttributeError('Имя или фамилия не из букв')
        if not value.istitle():
            raise AttributeError('Имя или фамилия не с заглавной буквы')


class GradeAndSubjectValidator:

    def __init__(self, min_value: int = None, max_value: int = None):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, _, name):
        self.private_item = '_' + name

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_item)

    def __set__(self, obj, value: dict):
        self._grade_validate(value)
        self._subject_validate(value)
        setattr(obj, self.private_item, value)

    def _grade_validate(self, value: dict):
        for value in value.values():
            for i in value:
                if not isinstance(i, int):
                    raise TypeError(f'Оценка {i} должна быть целым числом')
                if i is not None and i < self.min_value:
                    raise ValueError(f'Оценка {i} должна быть больше или равна {self.min_value}')
                if i is not None and i > self.max_value:
                    raise ValueError(f'Оценка {i} должна быть меньше или равна {self.max_value}')

    def _subject_validate(self, values: dict):
        data = self._read_csv()
        for value in values:
            if value not in data:
                raise AttributeError(f'Предмета нет в списке')

    def _read_csv(self) -> list:
        with open(FILE_NAME, 'r', encoding='utf-8') as f:
            reader = csv.reader(f, dialect='excel')
            return [row.pop() for row in reader][1:]


class Student:
    first_name: str = NameValidator()
    last_name: str = NameValidator()
    grades: dict = GradeAndSubjectValidator(MIN_GRADE, MAX_GRADE)
    tests: dict = GradeAndSubjectValidator(MIN_SCORE, MAX_SCORE)

    def __init__(self):
        self._first_name: str = ''
        self._last_name: str = ''
        self._grades: dict[str: tuple] = {}
        self._tests: dict[str: tuple] = {}

    def _mean_subjects(self, input_dict) -> dict:
        result = {key: round(mean(value), MEAN_ACCURACY) for key, value in input_dict.items()}
        result.update({'Средняя по всем': round(mean(result.values()), MEAN_ACCURACY)})
        return self._view_dict(result)

    def _view_dict(self, input_dict) -> str:
        return '\n'.join(f'{key}: {value}' for key, value in input_dict.items()) + '\n'

    def __str__(self):
        return f'\nСтудент: {self._first_name} {self._last_name}' \
               f'\n\nОценки по предметам:\n{self._view_dict(self._grades)}' \
               f'\n\nОценки по тестам:\n{self._view_dict(self._tests)}' \
               f'\nСредняя оценка по предметам:\n{self._mean_subjects(self._grades)}' \
               f'\nСредняя оценка по тестам:\n{self._mean_subjects(self._tests)}'


if __name__ == '__main__':
    student1 = Student()
    student1.first_name = 'Сергей'
    student1.last_name = 'Бодров'
    student1.grades = {'Литература': (5, 3, 4, 5, 3), 'Биология': (3, 3, 4, 5), 'Математика': (3, 5, 4, 5), 'Физика': (5, 5 ,5, 4, 4, 5, 3)}
    student1.tests = {'Математика': (75, 85, 90), 'Физика': (65, 75, 50, 80), 'Литература': (60, 40, 100), 'Химия': (70, 60, 80)}
    print(student1._mean_subjects(student1.grades))
    print(student1._mean_subjects(student1.tests))
    print(student1)
