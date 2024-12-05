<<<<<<< HEAD
class Life:
    def __init__(self):
=======
import pygame

class Life():
    def __init__(self, screen, max_lives=2):
        """ Initializes life system for the character
        args: screen (display) - creates the screen 
        max_lives (int) - initializes the number of 
        lives the character starts with
        """
        self.screen = screen
        self.max_lives = max_lives
        self.current_lives = max_lives
>>>>>>> f3895f4ad40f9ae55dc47f7a7362386d27b853a5
        
    def lose_life(self):
        self.x
        
<<<<<<< HEAD
    def check4rectangles():
        #if character pos == collidepoint(rect)
            #update_lives()
        
        
    def update_lives(self):
=======
    def lose_game(self):
        
>>>>>>> f3895f4ad40f9ae55dc47f7a7362386d27b853a5
