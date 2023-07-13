# Напишите для задачи 1 тесты pytest.
# Проверьте следующие варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)

import string
import pytest


def remove_chars(text: str) -> str:
    alpha = string.ascii_letters + ' '
    return ''.join(letter.lower() for letter in text if letter in alpha)


def test_remove_chars_no_change():
    assert remove_chars('dddddd dddd') == 'dddddd dddd'


def test_remove_chars_lower():
    assert remove_chars('AAA AA') == 'aaa aa'


def test_remove_chars_remove_punctuation():
    assert remove_chars('a,a,n: v.v;') == 'aan vv'


def test_remove_chars_remove_rus_alpha():
    assert remove_chars('БВАОПоаоваов') == ''


def test_remove_chars_remove_all():
    assert remove_chars('WWW,3322,ГГ:') == 'www'


# if __name__ == '__main__':
#     pytest.main(['-v'])
