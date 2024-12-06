import turtle
import pygame

class Character(pygame.sprite.Sprite):
    def __init__ (self, screen, color, x, y):
        """ Initializes character (rect) that will play game
        args: screen (display) - displays the screen
        color (string) - color of character
        x  (int) - x coordinate and width of character
        y (int) - y coordinate and height of character
        """
        super().__init__()
        self.screen = screen
        self.size = 20
        self.image = pygame.Surface([self.size, self.size])
        self.image.fill(color)

        self.color = color
       
        pygame.draw.rect(self.image, color, pygame.Rect(x, y, x, y))
        self.rect = self.image.get_rect()
    

    def create_character(self):
        """ Draws the rectangle that will be the character
        args: None
        returns: None
        """
        pygame.draw.rect(self.screen, self.color, self.rect)
        
    def move(self, key):
        """ Moves character based on the keyboard arrow hit (ex. up, down, right)
        args: key (event) - keyboard function
        returns: None
        """
        if key[pygame.K_RIGHT]:
            self.rect.x += 15   # Move right
        if key[pygame.K_UP]:
            self.rect.y -= 15  # Move up
        if key[pygame.K_DOWN]:
            self.rect.y += 15   # Move down
            