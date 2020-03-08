
class Player:
    def __init__(self):
        self.loc = 0
        #Player Stats
        #Health and Damage
        self.health = 20
        self.max_health = 20
        self.damage = 0
        #Gold and Inventory
        self.inventory = []
        self.max_inventory = 5
        self.gold_amt = 0
        #Chosen Stats
        (self.per_mod, self.dex_mod, self.dis_mod) = (2,2,2)

    def attack(monster):
        if (random.randrange(1,11) + self.dex_mod) > (random.randrange(1,11) + monster.dex_mod):
            monster.health -= self.damage #The player hits
            if monster.health <= 0:
                monster.die()
            else:
                return "You dealt {} damage!"
        else: #The player doesn't hit
            return "You missed!"

    def usePotion():
        potion_list = []
        for i in self.inventory:
            if isinstance(i, Potion):
                potion_list.append(i)
                print("[{}]==={}===".format(potion_list.index(i), i.name))
        p = input("Which potion?: ")
        while not (p.isdigit()) or not (0 <= p <= (len(potion_list) - 1)):
            p = input("Which potion?: ")
        potion = potion_list[p]
        potion.use()
        return "You used a {}".format(potion.name)

    def runAway(monster):
        if (random.randrange(1,11)) > (random.randrange(1,11) + monster.dex_mod + monster.per_mod):
            return True
        else:
            return False

    def sneak(monster):
        if (random.randrange(1,11) + dex_mod) > (random.randrange(1,11) + monster.per_mod):
            return True
        else:
            return False

    def die(self):
        print("You died!")
        input("Press [Enter] to continue")
        quit()
