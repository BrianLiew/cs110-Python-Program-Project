import random

class Artifact:
    def __init__(self):
        type = random.choice(["Ring", "Amulet", "Circlet", "Totem", "Talisman"])
        self.mod_type = random.choice(["PER", "DEX", "DIS", "MAX_H"])
        per_suffix = random.choice(["of Seeing Eyes", "of the Sage", "of Scrying", "of the Oracle"])
        dex_suffix = random.choice(["of the Scout", "of Winds", "of the Coward"])
        dis_suffix = random.choice(["of the Theif", "of Deft Hands", "of the Rogue"])
        max_h_suffix = random.choice(["of Iron Skin", "of the Warrior", "of Vitality"])
        rating = random.choices([("Common", 1), ("Superior", 2), ("Epic", 3), ("Divine", 4)], weights = [10,7,2,1])
        rating = rating[0]
        rating_name = rating[0]
        self.rating_mod = rating[1]

        if (self.mod_type == "PER"):
            self.name = rating_name + " " + type + " " + per_suffix
        elif (self.mod_type == "DEX"):
            self.name = rating_name + " " + type + " " + dex_suffix
        elif (self.mod_type == "DIS"):
            self.name = rating_name + " " + type + " " + dis_suffix
        elif (self.mod_type == "MAX_H"):
            self.name = rating_name + " " + type + " " + max_h_suffix

        self.vis_mod = random.randrange(0,4)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def look(self, player):
        if (random.randrange(1,11) + player.per_mod) > (random.randrange(1,11) + self.vis_mod):
            return True
        else:
            return False

    def add(self, player):
        if self.mod_type == "PER":
            player.per_mod += self.rating_mod
        elif self.mod_type == "DEX":
            player.dex_mod += self.rating_mod
        elif self.mod_type == "DIS":
            player.dis_mod += self.rating_mod
        elif self.mod_type == "MAX_H":
            player.max_health += self.rating_mod
        player.inventory.append(self)

    def drop(self):
        if self.mod_type == "PER":
            player.per_mod -= self.rating_mod
        elif self.mod_type == "DEX":
            player.dex_mod -= self.rating_mod
        elif self.mod_type == "DIS":
            player.dis_mod -= self.rating_mod
        elif self.mod_type == "MAX_H":
            player.max_health -= self.rating_mod
        player.inventory.remove(self)
