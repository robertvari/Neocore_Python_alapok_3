from turtle import color


class Dice:
    def __init__(self, sides, color):
        # private attributes
        self.__color = color
        self.__sides = sides

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, new_color):
        allowed_colors = ["white", "green", "blue"]
        #          if True does nothing else          print this
        assert new_color in allowed_colors, f"{new_color} as color is not allowed!!!"
        self.__color = new_color

    @property
    def sides(self):
        return self.__sides

    def __str__(self):
        return f"Sides: {self.__sides} Color: {self.__color}"

dice6 = Dice(6, "white")
print(dice6.color)
print(dice6.sides)

dice6.color = "green"
print(dice6)