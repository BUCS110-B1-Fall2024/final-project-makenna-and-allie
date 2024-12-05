import turtle
import pygame

class Character:
    def __init__ (self, screen, color):
        """ Initializes character (turtle) that will play game
        args: 
        screen (display) - screen of the maze
        color (string) - color of character
        """
        self.screen = screen
        self.color = color
        self.x = 10
        self.y = 10
        pygame.draw.rect(self.screen, self.color, (10,self.screen.get_height()/2, self.x, self.y))
        
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

