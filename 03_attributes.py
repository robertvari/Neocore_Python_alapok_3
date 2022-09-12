class Dice:
    # class attribute
    sides = 6
    color = "white"

class Car:
    # class attribute
    color = "black"
    wheels = 4
    doors = 5
    type = "Mercedes"
    licence_number = "ABC-345"


class Person:
    # class attribute
    name = "Robert"
    age = 45
    address = "Budapest"
    email = "robert@gmail.com"

my_car = Car()
print(my_car.color, my_car.wheels, my_car.doors, my_car.licence_number)

my_dice = Dice()
print(my_dice.color, my_dice.sides)

robert = Person()
print(robert.name, robert.age, robert.email, robert.address)