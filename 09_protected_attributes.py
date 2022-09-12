class Dice:
    def __init__(self, sides, color):
        # public level attributes
        self.sides = sides
        self.color = color

    def __str__(self) -> str:
        return f"Sides: {self.sides} Color: {self.color}"

class DiceProtected:
    def __init__(self, sides, color):
        # protected level attributes
        self._sides = sides
        self._color = color

    def __str__(self) -> str:
        return f"Sides: {self._sides} Color: {self._color}"

class DicePrivate:
    def __init__(self, sides, color):
        # private level attributes
        self.__sides = sides
        self.__color = color

    def __str__(self) -> str:
        return f"Sides: {self.__sides} Color: {self.__color}"

dice6 = Dice(6, "white")

dice10 = DiceProtected(10, "Green")

dice20 = DicePrivate(20, "Red")
print(dice20)
dice20.__color = "Yellow"
dice20.__sides = 100

print(dice20)