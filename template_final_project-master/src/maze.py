
import pygame
from src.cell import Cell
import random
import math

class Maze:
    
    def __init__(self, color, screen ):
        self.color = color
        self.screen = screen
        
    def drawRect(self):   
        for box in range(150,1150, 150):
            rand = random.randint(0, 500)
            rect = Cell(box, 0, self.screen, rand)
            rect.draw()
            
        
                
                
                
                
                
                
                
       # current_x = 0
        #current_y = 0
        #box = cell.Cell(current_x, current_y, self.screen, True)
        #box.draw(self.size)
    
            
            
        