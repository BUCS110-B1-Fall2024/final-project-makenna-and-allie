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
        
        self.gravity = 1
        self.velocity = 0
        self.jump_strength = -15
        self.is_jumping = False
        
    def create_character(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        
    def move_forward(self):
        """ Moves character forward repeatedly
        args: None
        return: None
        """
        self.velocity += self.gravity
        self.rect.y += self.velocity

        if self.rect.bottom > self.screen.get_height():
            self.rect.bottom = self.screen.get_height()

        if self.rect.top < 0:
            self.rect.top = 0
            
    def move_up(self):
        """ Moves character up 1
        args: None
        return: None
        """
        if not self.is_jumping: 
            self.velocity = self.jump_strength
            self.is_jumping = True


    #def redraw(self):
        

