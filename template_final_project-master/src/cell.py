import pygame

class Cell:
    
    def __init__(self, x, y, screen, visit, num, size):
        self.visit = visit
        self.color = 'purple'
        self.bord_col = 'white'
        self.screen = screen
        self.x = x
        self. y = y
        self.num = num
        self.size = size
        
        
    def draw(self):
        if self.visit == True:
            self.color = 'orange'
        pygame.draw.rect(self.screen, self.color, pygame.Rect(self.x, self.y, self.size, self.size))
        pygame.draw.rect(self.screen, self.bord_col, pygame.Rect(self.x, self.y, self.size, self.size),2)
        
    def get_num(self):
        print(self.num)
        
    def get_cord(self):
        print(f"x: {self.x}, y: {self.y}")
        
    def get_vist(self):
        print(self.visit)
        
    def carve(self):
        self.visit = True
        self.color = 'orange'
        Cell.draw()
        
        