import time, random


class Dice:
    # dunder method (special inherited method)
    def __init__(self, sides, color):
        # instance attribute
        self.sides = sides
        self.color = color
    
    # method of the Dice class
    def roll(self):
        print(f"Dice{self.sides} is rolling....")
        time.sleep(3)
        print(f"Current side: {random.randint(1, self.sides)}")

dice6 = Dice(6, "white")
dice6.roll()

dice20 = Dice(20, "blue")
dice20.roll()