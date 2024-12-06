
import pygame
from cell import Cell
import random
import math

class Maze:
    
    def __init__(self, color, screen):
        """ Initializes Maze class to form a random maze 
        each time and check for collisions
        args: color (string) - color of rectangles
        screen (display) - displays the screen
        """
        self.color = color
        self.screen = screen
        self.cells = []
        self.generate_maze()
        
    def generate_maze(self):   
        """ Generates a new randomized maze of rectangles
        args: None
        returns: None
        """
        height_options = [100, 150, 200, 250, 300, 350]
        
        for box in range(150,1150, 150):
            rand = random.choice(height_options)
            rect = Cell(box, 0, self.screen, rand)
            self.cells.append(rect)
    
    def draw_maze(self):
        """ Draws the newly randomized maze
        args: None
        returns: None
        """
        for cell in self.cells:
            cell.draw()
    
    def collision_checker(self, char_rect):
        """ Checks to see if a collision has occurred between rectangles
        args: char_rect (character) - the other rectangle, essentially the player
        returns: boolean value
        """
        for cell in self.cells:
            if char_rect.colliderect(cell.rect):
                return True
        return False