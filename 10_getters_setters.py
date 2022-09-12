from hashlib import new


class Dice:
    def __init__(self, sides, color):
        # private attributes
        self.__color = color
        self.__sides = sides
    
    # getter for sides
    def get_sides(self):
        return self.__sides

    def get_color(self):
        return self.__color

    # setter for the color attribute
    def set_color(self, new_color):
        allowed_colors = ["white", "green", "blue"]
        #          if True does nothing else          print this
        assert new_color in allowed_colors, f"{new_color} as color is not allowed!!!"

        self.__color = new_color

    def __str__(self) -> str:
        return f"Sides: {self.__sides} Color: {self.__color}"

dice6 = Dice(6, "white")
print(dice6.get_sides())
print(dice6.get_color())

dice6.set_color("yellow")
print(dice6)