import sys
import os
#sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))
import pygame 
from src.character import Character 
from src.setup import Setup
from src.maze import Maze
from src.button import Button


class Controller:
    
    
    def __init__(self):
        """
        Initializes objects and resoruces required to run program
        args: None
        """
        pygame.init()
        self.screen = pygame.display.set_mode((1200,600))
        pygame.display.set_caption('Maze')
        self.begin = Setup("black", self.screen)
        self.running = True 
        self.tom = Character(self.screen , 'blue', 50, 50)
        self.sprite = pygame.sprite.Group()
        self.sprite.add(self.tom)
        self.lose_button = Button(self.screen.get_width()/2- (500/2), self.screen.get_height()/2 - (200/2), 500, 200, 'red', self.screen, "You lost, Try again!", "Purple", 5)
        self.win_button = Button(self.screen.get_width()/2 - (500/2), self.screen.get_height()/2 - (200/2) , 500, 200, 'green', self.screen, "You Won, Congrats!", "Purple", 5)
        self.grid = Maze("White", self.screen)
        self.end_block = pygame.Rect(self.screen.get_width() - 15, 300, 20, 20)
        
        
    def mainloop(self):
        
        self.begin.create()
        pygame.display.flip()
        
        
        while self.running:
            #clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() 
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.if_begin()
                    self.create_maze()
                    pygame.draw.rect(self.screen, "orange", self.end_block)
                    self.sprite.draw(self.screen)
                if event.type == pygame.KEYDOWN:
                    key = pygame.key.get_pressed()
                    self.tom.move(key)
                    print(self.tom.rect.y)
                    print(self.tom.rect.x)
                    self.sprite.update()
                    #pygame.display.flip()
                    self.screen.fill('black') # clear screen
                    self.grid.draw_maze()#redraws maze
                    pygame.draw.rect(self.screen, "orange", self.end_block)
                    self.sprite.update()
                    pygame.display.flip()
                    self.sprite.draw(self.screen)  # Draw sprite on screen
                
                    if self.check_collision():
                        self.screen.fill('black')
                        self.lose_button.draw()
                        pygame.display.flip()
                        
                    if self.check_end():
                        self.screen.fill('black')
                        self.win_button.draw()
                        pygame.display.flip()
                        
                        
                self.sprite.update()
                pygame.display.flip()

        
    def if_begin(self):
       pos = pygame.mouse.get_pos()
       rect = pygame.Rect(50, 250, 545, 200)
       
       if rect.collidepoint(pos):
                        self.screen.fill('black')
       pygame.display.flip()
       
    def create_maze(self):
        #self.sprite.update()
        self.screen.fill('black') # clear screen
        self.grid.draw_maze() # redraw rect
        #self.sprite.draw(self.screen)  # Draw sprite on screen
        pygame.display.flip()
        
    def check_collision(self):
        """for y in range(self.tom.rect.top, self.tom.rect.bottom):
            for x in range(self.tom.rect.left, self.tom.rect.right):
                color_at_pixel = self.tom.screen.get_at((x, y))
                #print(color_at_pixel)
                # Check if the color at the current pixel matches the target color (purple)
                if color_at_pixel == (255, 255, 255, 255):
                    return True  # Collision detected

        return False  # No collision found
        """
        char_rect = self.tom.rect
        return self.grid.collision_checker(char_rect)
    
    def check_end(self):
        if self.tom.rect.x == 1185 and self.tom.rect.y == 300:
            return True
            
            
        
            

    
    