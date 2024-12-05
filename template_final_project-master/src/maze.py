
import pygame
from cell import Cell
import random
import math

class Maze:
    
    def __init__(self, screen, current_lives):
        """ Initializes the Maze class that will create our 
        maze of rectangles and check for collisions
        args: screen (display) - displays the screen
        current_lives (int) - current lives left for character
        """
        self.screen = screen
        self.current_lives = current_lives
        self.rectangles = []
        
    def drawRect(self):  
        """ Randomly draw different sized rectangles to form a maze
        args: None
        returns: None
        """ 
        for box in range(150, 1150, 150):
            rand = random.randint(0, 500)
            rect = Cell(box, 0, self.screen, rand)
<<<<<<< HEAD
            rect = Cell.Cell(box, 0, self.screen, rand)
            self.rectangles.append(rect)
=======
>>>>>>> 99724f452b2748f339fd641fe4190de17054aa59
            rect.draw()
    
    def check4rectangles(self, char_rect):
        """ Checks to se if our character has a collision in the maze
        args: char_rect (rectangle) - our character
        returns (boolean) - whether a collision occurred or not
        """
        for rect in self.rectangles:
            if char_rect.colliderect(rect.rect):
                self.current_lives.lose_life()
                return True
        return False
                
                
                
       # current_x = 0
        #current_y = 0
        #box = cell.Cell(current_x, current_y, self.screen, True)
        #box.draw(self.size)
    
            
            
        