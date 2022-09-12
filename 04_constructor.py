class Dice:
    def __init__(self, sides, color):
        # instance attribute
        self.sides = sides
        self.color = color


dice6 = Dice(sides=6, color="white")
print(dice6.sides, dice6.color)

dice10 = Dice(sides=10, color="blue")
print(dice10.sides, dice10.color)

dice20 = Dice(sides=20, color="red")
print(dice20.color, dice20.sides)