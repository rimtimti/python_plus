# Создайте класс окружность.
# Класс должен принимать радиус окружности при создании экземпляра.
# У класса должно быть два метода, возвращающие длину окружности и её площадь.

from math import pi
import doctest
import unittest
import pytest


class Circle:
    '''
    test_circle
    >>> circle = Circle(0)
    >>> circle.circumference()
    0.0
    >>> circle.area()
    0.0
    >>> circle = Circle(14)
    >>> circle.circumference()
    87.965
    >>> circle.area()
    615.752
    >>> circle = Circle(-10)
    >>> circle.circumference()
    62.832
    >>> circle.area()
    314.159
    >>> circle = Circle(10000000)
    >>> circle.circumference()
    62831853.072
    >>> circle.area()
    314159265358979.3
    '''
    ACCURACY = 3
    
    def __init__(self, radius):
        self.radius = abs(radius)

    def circumference(self):
        return round(2 * pi * self.radius, Circle.ACCURACY)

    def area(self):
        return round(pi * pow(self.radius, 2), Circle.ACCURACY)

class TestAccess(unittest.TestCase):

    def setUp(self):
        self.circle1 = Circle(0)
        self.circle2 = Circle(14)
        self.circle3 = Circle(-10)
        self.circle4 = Circle(10000000)

    def test_circumference(self):
        self.assertEqual(self.circle1.circumference(), 0)
        self.assertEqual(self.circle2.circumference(), 87.965)
        self.assertEqual(self.circle3.circumference(), 62.832)
        self.assertEqual(self.circle4.circumference(), 62831853.072)

    def test_area(self):
        self.assertEqual(self.circle1.area(), 0)
        self.assertEqual(self.circle2.area(), 615.752)        
        self.assertEqual(self.circle3.area(), 314.159)
        self.assertEqual(self.circle4.area(), 314159265358979.3)

    
def test_circle():
    circle1 = Circle(0)
    circle2 = Circle(14)
    circle3 = Circle(-10)
    circle4 = Circle(10000000)
    assert circle1.circumference() == 0
    assert circle2.circumference() == 87.965
    assert circle3.circumference() == 62.832
    assert circle4.circumference() == 62831853.072
    assert circle1.area() == 0
    assert circle2.area() == 615.752
    assert circle3.area() == 314.159
    assert circle4.area() == 314159265358979.3

if __name__ == '__main__':
    # circle = Circle(14)
    # print(f'{circle.circumference() = }\n{circle.area() = }')

    # doctest.testmod(verbose=True)
    # unittest.main(verbosity=True)
    pytest.main(['-v'])
