import turtle
import pygame

class Character(pygame.sprite.Sprite):
    def __init__ (self, screen, color, x, y):
        """ Initializes character (turtle) that will play game
        args: 
        screen (display) - displays the screen
        color (string) - color of character
        """
        super().__init__()
        self.screen = screen
        self.size = 20
        self.image = pygame.Surface([self.size, self.size])
        self.image.fill(color)

        self.color = color
       
        pygame.draw.rect(self.image, color, pygame.Rect(x, y, x, y))
        self.rect = self.image.get_rect()
        #self.rect.x = x
        #self.rect.y = y
        
    #def update(self):
        #self.velocity += self.gravity
        #self.rect.y += self.velocity
        
        
    
        
    def create_character(self):
        """ Draws the rectangle that will be the character
        args: None
        returns: None
        """
        pygame.draw.rect(self.screen, self.color, self.rect)
        
<<<<<<< HEAD
    def move(self,key):
        """ Moves character forward repeatedly
        args: None
        return: None
        """
        if key[pygame.K_RIGHT]:
            self.rect.x += 15   # Move right
        if key[pygame.K_UP]:
            self.rect.y -= 15  # Move up
        if key[pygame.K_DOWN]:
            self.rect.y += 15   # Move down
=======
>>>>>>> 4acec5b9be21dddafddba2f8b284b38454281166
    def move_forward(self):
        """ Moves character forward repeatedly, using gravity
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
        """ Moves character up, in a jumping motion
        args: None
        return: None
        """
        if not self.is_jumping: 
            self.velocity = self.jump_strength
            self.is_jumping = True


    #def redraw(self):
>>>>>>> 9700cb03bb4bc5fea2fc61c972355a22f0778b09
        

