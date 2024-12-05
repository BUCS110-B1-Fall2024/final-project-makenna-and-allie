import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))
import pygame 
from src.character import Character 
from src.setup import Setup
from src.maze import Maze

class Controller:
    
    def __init__(self):
        """
        Initializes objects and resoruces required to run program
        args: None
        """
        pygame.init()
        self.screen = pygame.display.set_mode((1200,600))
        pygame.display.set_caption('Maze')
        
        self.begin = Setup.Setup("black", self.screen)
        self.grid = Maze.Maze("white", self.screen)
        
        self.character = Character(self.screen)
        
        self.running = True
        
    def mainloop(self):
        """ Runs the game, using the Character and Trivia classes
        args: None
        returns: string - if you won the game
        """
        #1- Handle events
        """screen = pygame.display.set_mode((1200,600))
        pygame.display.set_caption('Maze')
        begin = setup.Setup("black", screen)
        """
        self.begin.create()
        pygame.display.flip()
        
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() 
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    rect = pygame.Rect(50, 450, 545, 200)
                    if rect.collidepoint(pos):
<<<<<<< HEAD
                        screen = pygame.display.set_mode((1200,800))
                        screen.fill('black')
                        grid = maze.Maze("white", screen)
                        grid.drawRect()
                        tom = character.Character(screen)
                        tom.set_color("blue")
=======
                        #screen = pygame.display.set_mode((1200,600))
                        self.screen.fill('black')
                        self.grid.drawRect()
                        self.character.set_color("blue")
>>>>>>> f3895f4ad40f9ae55dc47f7a7362386d27b853a5
                        pygame.display.flip()
                    
        #2. detect collisions and update models, ask character where
        # to move, etc.
        
        #3. Redraw next frame
        
        #4. Display next frame
        #pygame.display.flip()
 

    