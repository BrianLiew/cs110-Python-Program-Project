import random

class Gold:
    def __init__(self):
        self.amt = random.randrange(1,16)
        self.vis_mod = random.randrange(0,4)

    def __str__(self):
        return "{} gold".format(self.amt)

    def look(self, per_mod):
        if (random.randrange(1,11) + per_mod) > (random.randrange(1,11) + self.vis_mod):
            return True
        else:
            return False
