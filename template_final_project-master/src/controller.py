import pygame
from src import character 
from src import setup
from src import maze

class Controller:
<<<<<<< HEAD
=======
    from character import Character
>>>>>>> 9afc2476c767d885fb9132cb900d4a6b83e784f6
    
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
        screen = pygame.display.set_mode((1200,600))
        pygame.display.set_caption('Maze')
        begin = setup.Setup("black", screen)
        running = True
        
        begin.create()
<<<<<<< HEAD
       
=======
        grid = Maze.Maze("white", screen)
        grid.drawRect()
>>>>>>> 9afc2476c767d885fb9132cb900d4a6b83e784f6
        pygame.display.flip()
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
<<<<<<< HEAD
                    pygame.quit() 
=======
                    #pygame.quit() exit()
>>>>>>> 9afc2476c767d885fb9132cb900d4a6b83e784f6
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    rect = pygame.Rect(50, 450, 545, 200)
                    if rect.collidepoint(pos):
                        screen = pygame.display.set_mode((1200,600))
                        screen.fill('black')
<<<<<<< HEAD
                        grid = maze.Maze("white", screen)
                        grid.drawRect()
=======
                        grid = Maze.Maze(5,5, screen, 100,"white")
                        grid.drawGrid()
>>>>>>> 9afc2476c767d885fb9132cb900d4a6b83e784f6
                        pygame.display.flip()
                    
            
        #2. detect collisions and update models, ask character where
        # to move, etc.
        
        #3. Redraw next frame
        
        #4. Display next frame
        #pygame.display.flip()
    mainloop()
    
    