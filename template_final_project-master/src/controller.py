import sys
import os
#sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))
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
        
        self.begin = Setup("black", self.screen)
        self.grid = Maze("white", self.screen)
        self.character = Character(self.screen, "pink")
        
        self.gravity = 1
        self.jump_speed = -15
        self.velocity = 0
        self.game_over = False
        self.score = 0
        
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
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:  
                        self.character.move_up()
                        
        self.character.move_forward
        
        #2. detect collisions and update models, ask character where
        # to move, etc.
        self.grid.drawRect()
        if self.grid.check4rectangles(self.character.rect):
            if self.current_lives.lose_game():
                self.running = False
           
        self.screen.fill(0,0,0)
        self.character.create_character()
        self.grid.drawRect()
        self.curent_lives.display()
        
        pygame.display.flip()
        
        #3. Redraw next frame
        
        
        pygame.display.flip()
        #4. Display next frame
        #pygame.display.flip()
 

    