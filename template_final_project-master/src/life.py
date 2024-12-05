class Life:
<<<<<<< HEAD
    def __init__(self, screen, max_lives=3):
        """ Initializes Life class that will form the 
        system to keep track of how many lives our character
        has left, based off maze collisions
        args: screen (display) - displays the screen
        max_lives (int) - sets the number of lives the character starts
        with, which is 3
        """
        self.screen = screen
        self.max_lives = max_lives
        self.current_lives = max_lives
        
    def lose_life(self):
        """ Takes away one of the user's lives if
        they have any left
        args: None
        returns: None
        """
        if self.current_lives>0:
            self.lives-=1
        
    def lose_game(self):
        """ User loses the game if they hit zero lives
        args: None
        returns: None
        """
        self.lives
=======
    def __init__(self):
        
    #def lose_life(self):
        self.x
        
    #def check4rectangles():
        #if character pos == collidepoint(rect)
            #update_lives()
        
        
    #def update_lives(self):
        
>>>>>>> 99724f452b2748f339fd641fe4190de17054aa59
