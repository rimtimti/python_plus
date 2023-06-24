# Создайте класс окружность.
# Класс должен принимать радиус окружности при создании экземпляра.
# У класса должно быть два метода, возвращающие длину окружности и её площадь.

from math import pi


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
        return 2 * pi * self.radius

    def area(self):
        return pi * pow(self.radius, 2)


if __name__ == '__main__':
    circle = Circle(14)
    print(f'{circle.circumference() = }\n{circle.area() = }')
