class Character:
    import turtle
    
    def __init__ (self, x, y, img_file):
        """ Initializes character (turtle) that will play game
        args: 
        - x : int - starting x coordinate
        - y : int - starting y coordinate
        - img_file : str - maze file
        """
        self.turtle = turtle.Turtle()
        self.turtle.goto(x, y)
        self.file = img_file
        
    def move_left(self):
         """ Moves character left 1
        args: None
        return: None
        """
        x_coordinate = self.turtle.xcor()
        y_coordinate = self.turtle.ycor()
        self.turtle.goto(x_coordinate-1, y_coordinate)
    
    def move_right(self):
        """ Moves character right 1
        args: None
        return: None
        """
        x_coordinate = self.turtle.xcor()
        y_coordinate = self.turtle.ycor()
        self.turtle.goto(x_coordinate+1, y_coordinate)
        
    def move_forward(self):
        """ Moves character forward 1
        args: None
        return: None
        """
        x_coordinate = self.turtle.xcor()
        y_coordinate = self.turtle.ycor()
        self.turtle.goto(x_coordinate, y_coordinate+1)
        
    def move_backward(self):
        """ Moves character back 1
        args: None
        return: None
        """
        x_coordinate = self.turtle.xcor()
        y_coordinate = self.turtle.ycor()
        self.turtle.goto(x_coordinate, y_coordinate-1)
        
