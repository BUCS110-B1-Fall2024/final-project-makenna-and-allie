import pygame
from character import Character 
from setup import Setup
from maze import Maze

class Controller:
    from character import Character
    
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
        
    def mainloop(self):
        """ Runs the game, using the Character and Trivia classes
        args: None
        returns: string - if you won the game
        """
        #1- Handle events
        running = True
        
        self.begin.create()
        #grid = Maze.Maze("white", screen)
        grid.drawRect()
        pygame.display.flip()
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    #pygame.quit() exit()
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    rect = pygame.Rect(50, 450, 545, 200)
                    if rect.collidepoint(pos):
                        screen = pygame.display.set_mode((500,500))
                        screen.fill('black')
                        grid = Maze.Maze(5,5, screen, 100,"white")
                        grid.drawGrid()
                        pygame.display.flip()
                    
            
        #2. detect collisions and update models, ask character where
        # to move, etc.
        
        #3. Redraw next frame
        
        #4. Display next frame
        #pygame.display.flip()
    mainloop()
    
    