import pygame

class button(pygame.sprite.Sprite):
    def __init__(self, color, color2, x, y, width, height, text, fontSize):
        self.color = color
        self.color2 = color2
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.fontSize = fontSize
        self.mousePos = pygame.mouse.get_pos()
        self.mouseClick = pygame.mouse.get_pressed()
     
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 0)      
        buttonFont = pygame.font.SysFont("papyrus", self.fontSize)
        buttonText = buttonFont.render(self.text, False, (0, 0, 0))
        screen.blit(buttonText, ((self.x + (self.width//3.5)), (self.y + (self.height//4)))) 
        
    def isOver(self, mousePos, screen):
        if (self.mousePos[0] > self.x and mousePos[0] < self.x + self.width):
            if (self.mousePos[1] > self.y and mousePos[1] < self.y + self.height):
                pygame.draw.rect(screen, self.color2, (self.x, self.y, self.width, self.height), 0) 
                buttonFont = pygame.font.SysFont("papyrus", self.fontSize)
                buttonText = buttonFont.render(self.text, False, (0, 0, 0))
                screen.blit(buttonText, ((self.x + (self.width//3.5)), (self.y + (self.height//4))))
                return True
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 0)      
        buttonFont = pygame.font.SysFont("papyrus", self.fontSize)
        buttonText = buttonFont.render(self.text, False, (0, 0, 0))
        screen.blit(buttonText, ((self.x + (self.width//3.5)), (self.y + (self.height//4))))
        return False
        
    def isClicked(self, mousePos, mouseClick):
        if (self.mousePos[0] > self.x and mousePos[0] < self.x + self.width):
            if (self.mousePos[1] > self.y and mousePos[1] < self.y + self.height):
                if mouseClick[0] == 1:
                    return True
                return False
