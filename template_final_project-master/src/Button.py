import pygame



class Button:
    def __init__(self, x, y, width, height, color, screen, text, txtcolor, size):
        """ Initializes the Button class, which will be used to outline
        the beginning/setting screen of the game
        args: x (int) - starting x-coord of box
        y (int) - starting y-coord of box
        width (int) - width of bos
        height (int) - height of box
        color (string) - color of box
        screen (display) - displays the screen
        text (string) - what text will say
        txtcolor (string) - text color
        size (int) - size of text
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.color = color
        self.size = size
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.screen = screen
        self.text_font = pygame.font.SysFont("Arial", 20)
        self.text = text
        self.txt_color = txtcolor
        
       
        
    def __str__(self):
        """ Prints the width, height and color of the setting screen objects
        args: None
        returns: None
        """
        print(str(f"x = {self.width}, y = {self.height}, color = {self.color}"))
        
    def draw(self):
        """ Creates objects on setting screen that contain text in a box
        args: None
        returns: None
        """
        pygame.draw.rect(self.screen, self.color,  self.rect, self.size)  
        img = self.text_font.render(self.text, True, self.txt_color)
        self.screen.blit(img, (self.x,self.y))
        
        