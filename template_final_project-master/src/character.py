import turtle
import pygame

class Character(pygame.sprite.Sprite):
    def __init__ (self, screen, color, x, y):
        """ Initializes character (turtle) that will play game
        args: 
        screen (display) - screen of the maze
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
        pygame.draw.rect(self.screen, self.color, self.rect)
        
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
        

