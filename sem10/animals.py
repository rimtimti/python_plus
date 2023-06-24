# Доработайте задачу 5.
# Вынесите общие свойства и методы классов в класс Животное.
# Остальные классы наследуйте от него.
# Убедитесь, что в созданные ранее классы внесены правки.

# Создайте три (или более) отдельных классов животных. Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.


class Animal:
    def __init__(self, name: str, weight: int, age: int):
        self.name = name
        self.weight = weight
        self.age = age

    def move(self):
        pass

    def say(self):
        pass

    def __str__(self):
        return f'Класс: {str(self.__class__.__name__)} -> Имя: {self.name} Вес: {self.weight} Возраст: {self.age}'


class Bird(Animal):
    def __init__(self, name: str, weight: int, age: int, species: str, sound: str):
        super().__init__(name, weight, age)
        self.species = species
        self._sound = sound

    def move(self):
        return "Fly"

    def say(self):
        return self._sound

    def __str__(self):
        return f'{super().__str__()} Вид: {self.species} Говорит: {self._sound}'


class Dog(Animal):
    def __init__(self, name: str, weight: int, age: int, species: str):
        super().__init__(name, weight, age)
        self.species = species

    def move(self):
        return "Run"

    def say(self):
        return "Gov"

    def __str__(self):
        return f"{super().__str__()} Вид: {self.species}"


class Fish(Animal):
    def __init__(self, name: str, weight: int, age: int, species: str):
        super().__init__(name, weight, age)
        self.species = species

    def move(self):
        return "Swim"

    def say(self):
        return ""

    def __str__(self):
        return f"{super().__str__()} Вид: {self.species}"


if __name__ == '__main__':
    dog = Dog("Рэкс", 40, 5, "Такса")
    bird = Bird("Гоша", 1, 3, "Попугай", "Чирик")
    fish = Fish("Карп", 10, 5, "Речной")

    print(dog)
    print(bird)
    print(fish)