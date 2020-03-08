import random

class Monster:
    def __init__(self):
        difficulty = random.choices(["EASY", "MED", "HARD", "OUCH"], weights = [5,6,3,1])
        difficulty = difficulty[0]

        if difficulty == "EASY": #5
            self.health = random.randrange(5,10)
            self.damage = 5
            self.per_mod = 0
            self.dex_mod = 0
        elif difficulty == "MED": #10
            self.health = random.randrange(10,15)
            self.damage = 7
            self.per_mod = 1
            self.dex_mod = 1
        elif difficulty == "HARD": #15
            self.health = random.randrange(15,20)
            self.damage = 10
            self.per_mod = random.randrange(2,4)
            self.dex_mod = random.randrange(2,4)
        elif difficulty == "OUCH": #20
            self.health = 20
            self.damage = 12
            self.per_mod = random.randrange(3,5)
            self.dex_mod = random.randrange(3,5)

        name_adj = random.choice["Formidible", "Terrifying", "Grotestque", "Diseased", "Malformed", "Angry", "Rotten"]
        name_main = random.choice["Gargoyle", "Dungeon Slime", "Corpse Eater", "Deformity", "Cave Skulker", "Sewer Leech",
        "Shoggoth", "Shambler", "Flesh Maggot"]
        self.name = name_adj + " " + name_main

    def __str__(self):
        return self.name

    def attack(player):
        if (random.randrange(1,11) + self.dex_mod) > (random.randrange(1,11) + player.dex_mod):
            player.health -= self.damage #The monster hits
            if player.health <= 0:
                player.die()
            else:
                return "It dealt {} damage!"
        else: #The monster doesn't hit
            return "It missed!"

    def die(self):
        return "The {} dies!".format(self.name)
