import random

class Weapon:
    def __init__(self):
        rating = random.choices((("Shabby", -1),("Common", 0), ("Stalwart", 2), ("Rare", 3), ("Epic", 5)), weights = [50,30,20,5,1])
        rating = rating[0] #Determines how much damage it will do
        rating_name = rating[0]
        damage_mod = rating[1]

        type = random.choices([("Dagger", 3), ("Smallsword", 4), ("Broadsword", 5), ("Longsword", 7), ("Greatsword", 9)], weights = [2,3,3,2,1])
        type = type[0] #Determines how much the player's dex will decrease
        type_name = type[0]
        base_damage = type[1]

        self.damage = base_damage + damage_mod

        self.name = rating_name + " " + type_name

        self.vis_mod = random.randrange(0,4)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def look(self, per_mod):
        if (random.randrange(1,11) + per_mod) > (random.randrange(1,11) + self.vis_mod):
            return True
        else:
            return False

    def add(self, player):
        player.damage += damage_mod
        player.inventory.append(self)

    def drop(self, player):
        player.damage -= damage_mod
        player.inventory.remove(self)
