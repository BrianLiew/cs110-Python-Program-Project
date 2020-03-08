import pygame
from buttons import button

class controller:
    def __init__(self, width = 960, height = 720):
        pygame.init()
        pygame.font.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size())
        self.state = "INTRO"

    def mainLoop(self): #Main loop
        while True:
            if (self.state == "GAME"):
                self.gameLoop()
            elif (self.state == "INTRO"):
                self.introLoop()
            elif (self.state == "GAMEOVER"):
                self.gameOver()
                
    def introLoop(self): #Intro screen loop
        pygame.key.set_repeat(1,50)
        while (self.state == "INTRO"):
            self.background.fill((0, 0, 0))
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    sys.exit()
            self.mousePos = pygame.mouse.get_pos()
            self.mouseClick = pygame.mouse.get_pressed()
            gameIntroFont = pygame.font.SysFont("papyrus", 80)
            gameIntroMsg = gameIntroFont.render("Dungeon   Game", False, (255, 0, 0))
            self.screen.blit(gameIntroMsg, ((self.width//3.5), self.height//4))   
            pygame.display.flip()
            ### Start button generation
            startButton = button((50, 200, 50), (20, 150, 20), 192, 520, 192, 100, "Start", 50)
            startButton.isOver(self.mousePos, self.screen)
            if (startButton.isClicked(self.mousePos, self.mouseClick) == True):
                self.state = "GAME"
                self.gameLoop()
            ### Quit button generation
            quitButton = button((200, 50, 50), (170, 20, 20), 576, 520, 192, 100, "Quit", 50)
            quitButton.isOver(self.mousePos, self.screen)
            if (quitButton.isClicked(self.mousePos, self.mouseClick) == True):
                pygame.quit()        
            
    def gameLoop(self): #Game loop
        pygame.key.set_repeat(1,50)
        while (self.state == "GAME"):
            self.background.fill((0, 0, 0))
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    sys.exit()
            self.mousePos = pygame.mouse.get_pos()
            self.mouseClick = pygame.mouse.get_pressed()
            pygame.display.flip()
            fightButton = button((212, 175, 55), (182, 145, 25), 800, 630, 100, 45, "Fight", 25)
            fightButton.isOver(self.mousePos, self.screen)
            runButton = button((212, 175, 55), (182, 145, 25), 800, 540, 100, 45, "Run", 25)
            runButton.isOver(self.mousePos, self.screen)
            sneakButton = button((212, 175, 55), (182, 145, 25), 800, 450, 100, 45, "Sneak", 20)
            sneakButton.isOver(self.mousePos, self.screen)
            goldButton = button((212, 175, 55), (182, 145, 25), 650, 630, 100, 45, "Gold", 25)
            goldButton.isOver(self.mousePos, self.screen)
            trapsButton = button((212, 175, 55), (182, 145, 25), 650, 540, 100, 45, "Traps", 20)
            trapsButton.isOver(self.mousePos, self.screen) 
            itemsButton = button((212, 175, 55), (182, 145, 25), 650, 450, 100, 45, "Items", 20)
            itemsButton.isOver(self.mousePos, self.screen)              
	
    def gameOver(self): #Game over loop
        gameOverFont = pygame.font.SysFont(None, 50)
        gameOverMsg = gameOverFont.render("Game Over", False, (100, 0, 0))
        self.screen.blit(gameOverMsg, ((self.width/2), (self.height/2)))
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    sys.exit()
	    
