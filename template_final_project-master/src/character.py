import turtle

class Character:
    def __init__ (self, screen):
        """ Initializes character (turtle) that will play game
        args: 
        screen (display)- screen of the maze
        """
        self.turt = turtle.Turtle()
        self.turtle.goto(0, 0)
        self.screen = screen
        
        self.screen.listen()
        self.screen.onkey(self.move_forward, "Up")
        self.screen.onkey(self.move_backwards, "Down")
        self.screen.onkey(self.move_left, "Left")
        self.screen.onkey(self.move_right, "Right")
        
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

    #screen = turtle.Screen()
    #character = Character(screen)
    #screen.mainloop()
            
