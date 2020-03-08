import random

class Trap:
    def __init__(self):
        difficulty = random.choices(["EASY", "MED", "HARD", "OUCH"], weights = [5,6,3,1])
        difficulty = difficulty[0]

        if difficulty == "EASY":
            self.vis_mod = random.randrange(0,2)
            self.avoid_mod = random.randrange(0,2)
            self.dis_mod = random.randrange(0,2)
            self.damage = random.randrange(1,5)
            self.spite = 0
            trap_type = random.choice(["Falling Net", "Poison Dart"])
        elif difficulty == "MED":
            self.vis_mod = random.randrange(1,3)
            self.avoid_mod = random.randrange(1,3)
            self.dis_mod = random.randrange(1,3)
            self.damage = random.randrange(5,10)
            self.spite = 1
            trap_type = random.choice(["Arrow Volley", "Fire Breathing"])
        elif difficulty == "HARD":
            self.vis_mod = random.randrange(2,4)
            self.avoid_mod = random.randrange(2,4)
            self.dis_mod = random.randrange(2,4)
            self.damage = random.randrange(10,15)
            self.spite = 2
            trap_type = random.choice(["Spike Pit", "Collapsing Roof"])
        elif difficulty == "OUCH":
            self.vis_mod = random.randrange(3,5)
            self.avoid_mod = random.randrange(3,5)
            self.dis_mod = random.randrange(3,5)
            self.damage = random.randrange(15,20)
            self.spite = 3
            trap_type = random.choice(["Spike Wall", "Rolling Boulder"])

        self.name = trap_type + " Trap"
        self.is_live = True

    def __str_(self):
        return self.name

    def look(self,player):
        if (random.randrange(1,11) + vis_mod) < (random.randrange(1,11) + player.per_mod):
            return True
        else:
            return False

    def avoid(self,player):
        if (random.randrange(1,11) + avoid_mod) < (random.randrange(1,11) + player.dex_mod):
            return "You avoided the trap!"
        else:
            return self.spring(player)

    def disarm(self,player):
        if (random.randrange(1,11) + dis_mod) < (random.randrange(1,11) + player.dis_mod):
            self.is_live = False
            return "You disarmed the trap!"
        else:
            if random.randrange(1,6) <= self.spite:
                return self.spring(player)
            else:
                return "You could not disarm the trap"
                
    def spring(self, player):
        player.health -= self.damage
        self.is_live = False
        return "The {} dealt you {} damage!!".format(self.name, self.damage)
