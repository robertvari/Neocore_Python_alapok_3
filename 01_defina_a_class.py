class Dice:
    # class attribute
    sides = 6
    color = "white"

dice6 = Dice()

dice10 = Dice()
Dice.sides = 10
Dice.color = "Blue"

print(dice6.color)
print(dice10.color)