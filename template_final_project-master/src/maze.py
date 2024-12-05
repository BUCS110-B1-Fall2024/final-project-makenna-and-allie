
import pygame
from src.cell import Cell
import random
import math

class Maze:
    
    def __init__(self, color, screen, current_lives):
        self.color = color
        self.screen = screen
        self.current_lives = current_lives
        self.ractangles = []
        
    def drawRect(self):   
        for box in range(150,1150, 150):
            rand = random.randint(0, 500)
            rect = Cell(box, 0, self.screen, rand)
            rect.draw()
    
    def check4rectangles(self, char_rect):
        for rect in self.rectangles:
            if char_rect.colliderect(rect.rect):
                self.current_lives.lose_life()
                return True
        return False
                
                
                
       # current_x = 0
        #current_y = 0
        #box = cell.Cell(current_x, current_y, self.screen, True)
        #box.draw(self.size)
    
            
            
        