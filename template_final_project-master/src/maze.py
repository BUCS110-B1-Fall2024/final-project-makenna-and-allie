import pygame
from src import cell
import random


class Maze:
    
    def __init__(self, color, screen ):
        self.color = color
        self.screen = screen
        
    def drawRect(self):   
        
        rand = random.randint(0,100)
        rect = cell.Cell(10, 0, self.screen, rand)
            
        
                
                
                
                
                
                
                
       # current_x = 0
        #current_y = 0
        #box = cell.Cell(current_x, current_y, self.screen, True)
        #box.draw(self.size)
    
            
            
        