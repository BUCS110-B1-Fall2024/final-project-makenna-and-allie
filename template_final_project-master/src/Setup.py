import pygame
from button import Button

class Setup:
    
    def __init__(self, color, screen):
        """ Initializes Setup class which creates start screen
        args: color (string) - color of text
        screen (display) - displays the screen 
        """
        self.size = 1200
        self.color = color
        self.screen = screen
        
    def create(self):
        """ creates the start screen with text and tools
        args: None
        returns: None
        """
        pygame.display.flip()

        button1 = Button(50, 50, 1100, 255, 'blue', self.screen, "Get the Purple rect to the orange with out hitting the white!", 'red', 5)
        button1.draw()
        
        pygame.display.flip()

        button2 = Button(50, 325, 1100, 225, 'grey', self.screen, "Click to begin!", 'red', 5)
        
        button2.draw()

        pygame.display.flip()