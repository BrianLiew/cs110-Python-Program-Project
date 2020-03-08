from room import Room
from player import Player

class Map:
    def __init__(self, level, size):
        self.size = size
        self.level = level
        self.room_list = []
    def generate(self):
        for i in range(self.size + 1): #The last room will be where the player goes to the next level.
            self.room_list.append(Room(i)) #There will be nothing there, but a congratulatory message
        return self.room_list

    def spawnPlayer(self):
        self.the_player = Player()
        self.the_player.loc = 0

    def inhabitRoom(self):
        self.room_list[self.the_player.loc].run(self.the_player)
        self.movePlayer()

    def movePlayer(self): #Move player to the next room
        self.the_player.loc += 1
        if self.the_player.loc < self.size:
            self.inhabitRoom()
        else:
            print("You made it!!!")
            input("Press [Enter] to continue")
            quit()
