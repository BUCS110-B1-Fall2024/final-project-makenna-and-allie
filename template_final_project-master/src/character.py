class Character:
    import turtle
    import pygame
    
    def __init__ (self, screen):
        """ Initializes character (turtle) that will play game
        args: 
        screen (display)- screen of the maze
        """
        self.turt = turtle.Turtle()
        self.turtle.goto(0, 0)
        self.screen = screen
        
    def move_forward(self):
        """ Moves character forward 1
        args: None
        return: None
        """
        self.turtle.setheading(90)
        self.turtle.forward(1)

    def move_backwards(self):
        """ Moves character back 1
            args: None
            return: None
            """
        self.turtle.setheading(270)
        self.turtle.forward(1)

    def move_left(self):
        """ Moves character left 1
        args: None
        return: None
        """
        self.turtle.setheading(180)
        self.turtle.forward(1)

    def move_right(self):
        """ Moves character right 1
        args: None
        return: None
        """
        self.turtle.setheading(0)
        self.turtle.forward(1)

    self.screen.listen()
    self.screen.onkey(move_forward, "Up")
    self.screen.onkey(move_backwards, "Down")
    self.screen.onkey(move_left, "Left")
    self.screen.onkey(move_right, "Right")

    self.screen.mainloop()
            
