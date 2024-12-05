import turtle
import pygame

class Character:
    def __init__ (self, screen):
        """ Initializes character (turtle) that will play game
        args: 
        screen (display)- screen of the maze
        """
        self.turtle = turtle.Turtle()
        self.screen = screen
        #self.turtle.penup()
        #self.turtle.goto(0, -100)
        #self.speed = 5
        
        self.screen.listen()
        self.screen.onkey(self.move_forward, "Up")
        self.screen.onkey(self.move_backwards, "Down")
        self.screen.onkey(self.move_left, "Left")
        self.screen.onkey(self.move_right, "Right")
        
        self.move_forward()
    
    def move_forward(self):
        """ Moves character forward repeatedly
        args: None
        return: None
        """
        self.turtle.forward(self.speed)
        self.screen.ontimer(self.move_forward, 30)
        
    def move_up(self):
        """ Moves character up 1
        args: None
        return: None
        """
        self.turtle.setheading(90)

    def move_down(self):
        """ Moves character down 1
        args: None
        return: None
        """
        self.turtle.setheading(270)

    #screen = turtle.Screen()
    #character = Character(screen)
    #screen.mainloop()
    
