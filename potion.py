import random

class Potion:
    def __init__(self):
        rating = random.choices((("Small", 5), ("Common", 10), ("Superior", 20), ("Giant", 30)), weights = [10,7,3,2])
        rating = rating[0] #Determines how much it'll heal you
        rating_name = rating[0]
        self.health_inc = rating[1]

        self.name = rating_name + " Potion of Healing"

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
        player.inventory.append(self)

    def drop(self, player):
        player.inventory.remove(self)

    def use(self, player):
        if ((player.health + health_inc) > max_health):
            player.health = max_health
        else:
            player.health += health_inc
        drop(self, player)
