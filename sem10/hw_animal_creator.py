# Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.

from animals import Animal, Dog, Bird, Fish


class AnimalsCreator(Dog, Bird, Fish, Animal):

    def create(__name__, name: str, weight: int, age: int, species=False, sound=False):
        animal = Animal(name, weight, age)
        if sound:
            animal = __name__(name, weight, age, species, sound)
        elif species:
            animal = __name__(name, weight, age, species)
        return animal


if __name__ == '__main__':
    print(AnimalsCreator.create(Bird, 'Гоша', 10, 3, 'Попугай', 'Привет'))
    print(AnimalsCreator.create(Dog, 'Мухтар', 10, 3, 'Овчарка'))
    print(AnimalsCreator.create(Fish, 'Вася', 5, 1, 'Окунь'))
    print(AnimalsCreator.create(Animal, 'Нечто', 3, 2))
