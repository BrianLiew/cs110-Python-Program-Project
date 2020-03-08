from map import Map #This should be the only file imported?!
import pygame

def main():
    map1 = Map(1, 10)
    map1_rooms = map1.generate() #Returns the map as a list of its rooms
    player1 = map1.spawnPlayer()
    map1.inhabitRoom()
main()
