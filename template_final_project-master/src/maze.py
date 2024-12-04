import pygame
from src import button

class Maze:
    
    def __init__(self, rows, cols, screen, size):
        self.row = rows
        self.col = cols
        self.screen = screen
        self.color = 'white'
        self.size = size
        
    def drawGrid(self):
        for x in range(self.size, self.screen.get_width(), self.size):
            pygame.draw.line(self.screen, self.color, (x, 0), (x, self.screen.get_height()),2)
        for y in range(self.size, self.screen.get_height(), self.size):
            pygame.draw.line(self.screen, self.color, (0, y), (self.screen.get_width(), y),2)
    
            
            
        