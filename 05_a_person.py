class Character:
    def __init__(
        self, 
        name, 
        player_name, 
        race, 
        strength=100, 
        constitution=10, 
        intelligence=10, 
        wisdom=10, 
        charisma=10
    ):
        
        self.name = name
        self.player_name = player_name
        self.race = race
        self.strength = strength
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma


mordred = Character("Mordred", "Robert", "Human")
print(mordred.name, mordred.player_name, mordred.race, mordred.wisdom)

sauron = Character("Sauron", "Gandalf", "Mage", strength=1000, constitution= 100, intelligence=10000, charisma=1)
print(sauron.name, sauron.player_name, sauron.charisma)