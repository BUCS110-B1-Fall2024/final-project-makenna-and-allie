class Controller:
    import character from character
    import trivia from Trivia
    
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
        while(True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() exit()
        #2. detect collisions and update models, ask character where
        # to move, etc.
        #3. Redraw next frame
        #4. Display next frame
        pygame.display.flip()
        
    
    