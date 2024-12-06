
import pygame
from src.cell import Cell
import random
import math

class Maze:
    
    def __init__(self, color, screen):
        self.color = color
        self.screen = screen
        self.cells = []
        self.generate_maze()
        
    def generate_maze(self):   
        """for box in range(150,1150, 150):
            rand = random.randint(0, 500)
            rect = Cell(box, 0, self.screen, rand)
            rect.draw()
            """
        height_options = [100, 150, 200, 250, 300, 350]
        
        for box in range(150,1150, 150):
            rand = random.choice(height_options)
            rect = Cell(box, 0, self.screen, rand)
            self.cells.append(rect)
    
    def draw_maze(self):
        for cell in self.cells:
            cell.draw()
    
    def collision_checker(self, char_rect):
        for cell in self.cells:
            if char_rect.colliderect(cell.rect):
                return True
        return False