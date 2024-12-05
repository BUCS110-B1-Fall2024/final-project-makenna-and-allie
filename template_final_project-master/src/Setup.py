import pygame 
from src import button



class Setup:
    
    def __init__(self, color, screen):
        self.size = 1200
        self.color = color
        self.screen = screen
        
    def create(self):
        
        #screen = pygame.display.set_mode((pygame.display.Info().current_w, pygame.display.Info().current_h),pygame.FULLSCREEN)
        
        
        #screen.fill(self.color)
        
        pygame.display.flip()

        button1 = button.Button(50, 30, 1100, 200, 'blue', self.screen, "Directions:", 'red', 5)
        button1.draw()
        
        pygame.display.flip()

        button2 = button.Button(50, 250, 545, 200, 'grey', self.screen, "Click to begin!", 'red', 5)
        
        button2.draw()

        pygame.display.flip()

        button3 = button.Button(605, 250, 182, 200, 'white', self.screen, "Easy", "white", 5)
        button4 = button.Button(787, 250, 182, 200, 'white', self.screen, "Medium", "white", 5)
        button5 = button.Button(968, 250, 182, 200, 'white', self.screen, "Hard", "white", 5)
        button3.draw()
        button4.draw()
        button5.draw()

        pygame.display.flip()
                    