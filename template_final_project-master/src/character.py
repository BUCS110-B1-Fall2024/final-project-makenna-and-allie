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
        
<<<<<<< HEAD
       # self.screen.listen()
        #self.screen.onkey(self.move_forward, "Up")
        #self.screen.onkey(self.move_backwards, "Down")
        #self.screen.onkey(self.move_left, "Left")
        #self.screen.onkey(self.move_right, "Right")
        
        #self.move_forward()
    
=======
        self.gravity = 1
        self.velocity = 0
        self.jump_strength = -15
        self.is_jumping = False
        
    def create_character(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        
>>>>>>> 4acec5b9be21dddafddba2f8b284b38454281166
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
        

