import pygame
from character import Character 
from trivia import Trivia 
from Setup import Setup
from maze import Maze

class Controller:
    from character import Character
    from trivia import Trivia
    
    def __init__(self):
        """
        Initializes objects and resoruces required to run program
        args: None
        """
        
    def mainloop(self):
        """ Runs the game, using the Character and Trivia classes
        args: None
        returns: string - if you won the game
        """
        #1- Handle events
        screen = pygame.display.set_mode((1200,1200))
        pygame.display.set_caption('Maze')
        begin = Setup.Setup("black", screen)
        running = True
        
        begin.create()
        pygame.display.flip()
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    #pygame.quit() exit()
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    screen = pygame.display.set_mode((1200,1200))
                    screen.fill('black')
                    grid = Maze.maze(5,5, screen, 50)
                    grid.drawGrid()
                    pygame.display.flip()
                    
            
        #2. detect collisions and update models, ask character where
        # to move, etc.
        
        #3. Redraw next frame
        
        #4. Display next frame
        #pygame.display.flip()
        
    
    