class Character:
    def __init__(self, name, player_name, race, strength=100, constitution=10, intelligence=10, wisdom=10, charisma=10):
        self.name = name
        self.player_name = player_name
        self.race = race
        self.strength = strength
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma

    # class method/function
    def show_status(self):
        print("-"*50, f"{self.name} Status", "-"*50,)
        print(f"Name: {self.name}")
        print(f"Race: {self.race}")
        print(f"Strength: {self.strength}")
        print(f"Constitution: {self.constitution}")
        print(f"Intelligence: {self.intelligence}")
        print(f"Wisdom: {self.wisdom}")
        print(f"Charisma: {self.charisma}")
        print("-" * 100)

    def attack(self, other):
        print(f"{self.name} attacks {other.name}!!!!")


mordred = Character("Mordred", "Robert", "Human")
# mordred.show_status()

sauron = Character("Sauron", "Gandalf", "Mage", strength=1000, constitution= 100, intelligence=10000, charisma=1)
# sauron.show_status()

mordred.attack(sauron)
sauron.attack(mordred)