class Character_Base:
    def __init__(self, name, race, age):
        self.name = name
        self.race = race
        self.age = age

    def say_hello(self):
        print(f"Hello, my name is {self.name}")


class Hero(Character_Base):
    pass

class NPC(Character_Base):
    pass

class Enemy(Character_Base):
    pass

class Dog(Character_Base):
    # override the base class say_hello
    def say_hello(self):
        print("Vuff Vuff")

class Bird(Character_Base):
    # override the base class say_hello
    def say_hello(self):
        print("Csip csip")


mordred = Hero("Mordred", "Human", 18)
bodri = Dog("Bodri", "dog", 5)
old_lady = NPC("Granny", "Human", 89)
parrot = Bird("Black Bird", "bird", 3)

mordred.say_hello()
old_lady.say_hello()
bodri.say_hello()
parrot.say_hello()