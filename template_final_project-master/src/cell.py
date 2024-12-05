import pygame

class Cell:
    
    def __init__(self, x, y, screen, height):
        self.color = 'purple'
        self.bord_col = 'white'
        self.screen = screen
        self.x = x
        self. y = y
        self.height = height 
        
    def draw(self):
        pygame.draw.rect(self.screen, self.color, pygame.Rect(self.x, self.y, 10, self.height))
        #pygame.draw.rect(self.screen, self.bord_col, pygame.Rect(self.x, self.y, 10, self.height),2)
        

        
    def get_cord(self):
        print(f"x: {self.x}, y: {self.y}")
        
        
        