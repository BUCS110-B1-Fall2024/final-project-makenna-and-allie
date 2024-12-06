import pygame
from src.button import Button

class Setup:
    
    def __init__(self, color, screen):
        self.size = 1200
        self.color = color
        self.screen = screen
        
    def create(self):
        
        #screen = pygame.display.set_mode((pygame.display.Info().current_w, pygame.display.Info().current_h),pygame.FULLSCREEN)
        
        
        #screen.fill(self.color)
        
        pygame.display.flip()

        button1 = Button(50, 50, 1100, 255, 'blue', self.screen, "Get the Purple rect to the orange with out hitting the white!", 'red', 5)
        button1.draw()
        
        pygame.display.flip()

        button2 = Button(50, 325, 1100, 225, 'grey', self.screen, "Click to begin!", 'red', 5)
        
        button2.draw()

        pygame.display.flip()