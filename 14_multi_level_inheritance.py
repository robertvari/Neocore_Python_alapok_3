class Character_Base:
    def __init__(self, name, race, age):
        self.name = name
        self.race = race
        self.age = age

    def say_hello(self):
        print(f"Hello, my name is {self.name}")

class Hero(Character_Base):
    pass


class Animal(Character_Base):
    def eat(self):
        print(f"{self.name} is eating")

class Dog(Animal):
    pass

class Bird(Animal):
    pass

bodri = Dog("Bodri", "dog", 10)
parrot = Bird("Black Bird", "animal", 3)

bodri.eat()
parrot.eat()