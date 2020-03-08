:warning: Everything between << >> needs to be replaced (remove << >> after replacing)
# Dungeon Game

## CS 110 Final Project
### Fall, 2019
### [Assignment Description](https://drive.google.com/open?id=1HLIk-539N9KiAAG1224NWpFyEl4RsPVBwtBZ9KbjicE)

https://github.com/bucs110/final-project-fall19-final-team

<< [link to demo presentation slides](#) >>

### Team: Final Team
#### 1.Robert Berland
#### 2.Brian Liew
#### 3.Alex Carter

***

## Project Description
Dungeongame is a text-based rouge-like RPG where the player navigates a series of rooms infested with traps and monsters. Actions such as disarming traps, fighting monsters and looking for gold are done in a way similar to skill checks in the tabletop games from which this game is inspired. Two random numbers are generated, modifiers are added, and the numbers are compared to see whether or not the action is performed successfully. For example, the player wants to avoid a trap; the player has a dexterity modifier of +4 and the trap has an avoid modifier of +3; the player rolls a 5, and the trap rolls a 3. 5+4 = 9, 3+3 = 6, 9 > 6, therefore the player successfully avoids the trap. Throughout the rooms, gold and items can be found. Items give the player buffs that allow them to better perform their actions, and gold is tallied at the end of the game for a total score. 
 
***    

## User Interface Design
* << A wireframe or drawing of the user interface concept along with a short description of the interface. You should have one for each screen in your program. >>
    * For example, if your program has a start screen, game screen, and game over screen, you should include a wireframe / screenshot / drawing of each one and a short description of the components
* << You should also have a screenshot of each screen for your final GUI >>

***        

## Program Design
* Non-Standard libraries
    * Pygame (https://www.pygame.org/) - A module set incorporating many common game development functions into python, developed by Pete Shinners and Pygame Community. Includes crucial graphical elements as well as a musical playback functionality.	

     
* Class Interface Design
    *Class Flowchart 
        * ![class diagram](https://github.com/bucs110/final-project-fall19-final-team/blob/master/assets/DungeonGame.png)
    
* Classes
   * 1._Player_
          
        *The player class contains the health the player starts with, aswell as the damage that the player can do to other classes. The class also contains three modifiers, Perception, Disarm, and Dexterity. These modifiers are randomly generated and demonstrate the players abilities to see something, to disarm a trap, and agility of a player which is used when avoiding traps. On top of this the player has an inventory where the gold collected will be stored. Using all these abilities the player has three functions, fight(), sneak(), and attack() which help destroy monsters, disarm, or sneak by traps.
   * 2._Trap_
          
        *The trap class contains the damage that it will inflict on the player. It also contains three modifiers, Visibility, Avoid, and Disarm. These modifiers demonstrate how difficult it is to see the trap, how difficult it is to avoid the trap, and how difficult it is to disarm the trap. This class also has is_live which determines whether the trap is active or inactive. There are 4 functions find(), avoid(), disarm(), spring(), which are used in the class to determine whether the trap was found, was avoided, disarmed, or should deal damage to the player.
   * 3._Monster_
   
        *The monster class contains the monsters health, damage it can deal on the player, the Dexterity and Perception modifiers, and two functions, attack() which tells the monster to attack the player, or die() which is called when the player kills the monster in battle.
   * 4._Item_
   
        *Items can be collected by the player and can boost the players abilities, like its health, damage, Perception, Dexterity, and Disarm modifiers. Items can be found, added to a players inventory or dropped if the player doesn't want to hold it in the inventory or there isn't enough room to add another item.
   * 5._Gold_
   
        *The gold class contains the amount of gold a player finds, the visibility modifier of the gold, and two functions, find() and add(). Once the player finds gold depending on his Perception modifier and the Gold's visibility, it can add whatever amount the gold was to the player's gold.
   * 6._Room_
   
        *Rooms can have good encounters or bad encounters for the player which means that either the room could have something good like gold, or it can have a monster or trap waiting for the player. This class contains the loction of the room and where the next room will be.
   * 7._Map_
        
        *The map has a size, difficulty, and end location of the game. This class will determine how difficult it will be to defeat monsters, and disarm traps, aswell as where the game will end for the player.
***

## Tasks and Responsibilities
* You must outline the team member roles and who was responsible for each class/method, both individual and collaborative.

### Software Lead - Robert Berland

<< Worked as integration specialist by... >>

### Front End Specialist - Brian Liew

<< Front-end lead conducted significant research on... >>

### Back End Specialist - Alex Carter

<< The back end specialist... >>

## Testing
* << Describe your testing strategy for your project. >>
    * << Example >>

* Your ATP

| Step                  | Procedure     | Expected Results  | Actual Results |
| ----------------------|:-------------:| -----------------:| -------------- |
|  1  | Run Counter Program  | GUI window appears with count = 0  |          |
|  2  | click count button  | display changes to count = 1 |                 |
etc...
