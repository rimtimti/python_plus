# Напишите для задачи 1 тесты unittest.
# Проверьте следующие варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)

import string
import unittest


def remove_chars(text: str) -> str:
    alpha = string.ascii_letters + ' '
    return ''.join(letter.lower() for letter in text if letter in alpha)


class TestRemoveChars(unittest.TestCase):
    def test_no_change(self):
        self.assertEqual(remove_chars('dddddd dddd'), 'dddddd dddd')

    def test_lower(self):
        self.assertEqual(remove_chars('AAA AA'), 'aaa aa')

    def test_punctuation(self):
        self.assertEqual(remove_chars('a,a,n: v.v;'), 'aan vv')

    def test_rus_alpha(self):
        self.assertEqual(remove_chars('БВАОПоаоваов'), '')

    def test_all(self):
        self.assertEqual(remove_chars('WWW,3322,ГГ:'), 'www')


# if __name__ == '__main__':
#     unittest.main(verbosity=True)
