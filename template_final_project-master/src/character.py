import turtle
import pygame

class Character(pygame.sprite.Sprite):
    def __init__ (self, screen, color, w, h):
        """ Initializes character (turtle) that will play game
        args: 
        screen (display) - screen of the maze
        color (string) - color of character
        """
        super().__init__()
        self.screen = screen
        self.image = pygame.Surface([w,h])
        self.image.fill(color)

        self.color = color
        self.x = 10
        self.y = 500
        pygame.draw.rect(self.image, color, pygame.Rect(self.x, self.y, w, h))
        self.rect = self.image.get_rect()
        
       # self.screen.listen()
        #self.screen.onkey(self.move_forward, "Up")
        #self.screen.onkey(self.move_backwards, "Down")
        #self.screen.onkey(self.move_left, "Left")
        #self.screen.onkey(self.move_right, "Right")
        
        #self.move_forward()
    
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

