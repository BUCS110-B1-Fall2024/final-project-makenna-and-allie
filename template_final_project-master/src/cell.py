import pygame

class Cell:
    def __init__(self, x, y, screen, height):
        """ Initializes the Cell class, which will be used to create
        different versions of mazes
        args: x (int) - xy coordinate of rect
        y (int) - y coordinate of rect
        screen (display) - displays the screen 
        height (int) - height of rect
        """
        self.color = 'white'
        self.bord_col = 'white'
        self.screen = screen
        self.x = x
        self. y = y
        self.height = height 
        self.rect = pygame.Rect(x, y, 50, self.height)
        
    def draw(self):
        """ Forms a rectangle/barrier in maze
        args: None
        returns: None
        """
        pygame.draw.rect(self.screen, self.color, pygame.Rect(self.x, self.y, 50, self.height))
        pygame.draw.rect(self.screen, self.bord_col, pygame.Rect(self.x, self.y, 50, self.height),2)
        scr_h =  self.screen.get_height()
        bottom = scr_h - (self.height + 40)
        pygame.draw.rect(self.screen, self.color, pygame.Rect(self.x , self.y + self.height + 40, 50, bottom))
        pygame.draw.rect(self.screen, self.bord_col, pygame.Rect(self.x, self.y + self.height + 40, 50, bottom),2)
        
    def get_cord(self):
        """ Prints the coordinates of the rectangle created
        args: None
        returns: None
        """
        print(f"x: {self.x}, y: {self.y}")
        
        
        