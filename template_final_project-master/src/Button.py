import pygame



class Button:
    
    def __init__(self, x, y, width, height, color, screen, text, txtcolor, size):
        
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.color = color
        self.size = size
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.screen = screen
        self.text_font = pygame.font.SysFont("Arial", 50)
        self.text = text
        self.txt_color = txtcolor
        
       
        
    def __str__(self):
        
        print(str(f"x = {self.width}, y = {self.height}, color = {self.color}"))
        
    def draw(self):
        
        pygame.draw.rect(self.screen, self.color,  self.rect, self.size)  
        img = self.text_font.render(self.text, True, self.txt_color)
        self.screen.blit(img, (self.x,self.y))
        
        