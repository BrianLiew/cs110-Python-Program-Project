from gold import Gold
from weapon import Weapon
from potion import Potion
from artifact import Artifact
from player import Player
from monster import Monster
from trap import Trap

import random

class Room:
    def __init__(self, loc):
        self.loc = loc

    def __repr__(self):
        return "room_{}".format(self.loc)

    def run(self, player):
        print("=== This is room {} ===".format(self.loc))

        def generateEncounter():
            enc_dict = {}

            if random.choice([True, False]): #Generates Gold
                g = Gold()
            else:
                g = None
            enc_dict["gold"] = g

            if random.choice([True, False]): #Generates items
                i = random.choice([Weapon(), Potion(), Artifact()])
            else:
                i = None
            enc_dict["item"] = i

            if random.choice([True,False]):
                enc_dict["monster"] = Monster()
                enc_dict["trap"] = None
            else:
                enc_dict["trap"] = Trap()
                enc_dict["monster"] = None

            return enc_dict
        self.encounters = generateEncounter()

        if self.encounters["monster"] == None:
            self.actions = "MAIN"
        else:
            self.actions = "MONST"


    ############ THE PLAYERS AVAILABLE ACTIONS ARE DEFINED HERE ############

    ###### MAIN ACTIONS ######

        def mainActions():
            def look():
                self.actions = "LOOK"

            def nextRoom():
                t = self.encounters["trap"]
                if t != None:
                    message = t.spring(player)
                    self.actions = ""
                    return message

                else:
                    self.actions = ""


    ###### LOOK ACTIONS ######

        def lookActions():
            def lookForGold():
                g = self.encounters["gold"]
                if g == None:
                    return "There's no gold here"
                else:
                    if g.look(player.per_mod) == True:
                        self.actions = "LOOT -g"
                        return "You found {}!".format(g.__str__())
                    else:
                        self.encounters["gold"] = None
                        return "There's no gold here"

            def lookForItems():
                i = self.encounters["item"]
                if i == None:
                    return "There are no items here"
                else:
                    if i.look(player) == True:
                        self.actions = "LOOT -i"
                        return "You found [{}]".format(i.__str__())
                    else:
                        self.encounters["item"] = None
                        return "There are no items here"

            def lookForTraps():
                t = self.encounters["trap"]
                if t == None:
                    return "There are no traps here"
                else:
                    if t.look(player) == True:
                        self.actions = "TRAP"
                        return "You found a {}!".format(t.__str__())
                    else:
                        return "There are no traps here"

    ###### LOOT ACTIONS ######

        def lootActions(loot):
            def take():
                l = self.encounters.get(loot)
                if loot == "gold": #If it's gold
                    player.gold_amt += l.amt
                elif loot == "item": #If it's an item
                    if ((player.inventory + 1) > player.max_inventory):
                        return "You're carrying too much stuff!"
                    else:
                        l.add(player) #Add to inventory
                message = "You added '{}' to your inventory".format(l)
                self.encounters[loot] = None
                self.actions = "MAIN"
                return message


            def leave():
                self.actions = "MAIN"

    ###### MONSTER ACTIONS ######

        def monsterActions():
            def fight():
                self.actions = "FIGHT"
            def sneak():
                if player.sneak(monster):
                    nextRoom()
                else:
                    self.actions = "FIGHT"
                    return monster.attack(player)

    ###### FIGHT ACTIONS ######

        def fightActions():
            def attack():
                m = self.encounters["monster"]
                player.attack(m)
                m.attack(player)

            def usePotion():
                player.usePotion()

            def runAway():
                if player.runAway(monster):
                    nextRoom()
                else:
                    return monster.attack(player)

    ###### TRAP ACTIONS ######

        def trapActions():
            t = self.encounters["trap"]
            def avoid():
                return t.avoid(player)

            def disarm():
                return t.disarm(player)

            def turnBack():
                self.actions = "MAIN"


    ############ MENU OPTIONS LOOPS ############

        while self.actions == "MAIN":
            mainActions()

        while self.actions == "LOOK":
            lookActions()

        while self.actions == "LOOT -g":
            lootActions("gold")

        while self.actions == "LOOT -i":
            lootActions("item")

        while self.actions == "MONST":
            monsterActions()

        while self.actions == "FIGHT":
            fightActions()

        while self.actions == "TRAP":
            trapActions()
