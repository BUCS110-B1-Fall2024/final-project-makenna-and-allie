import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))
import pygame
from src.controller import Controller
#import your controller

def main():
    pygame.init()
    control = Controller()
    control.mainloop()
    #Create an instance on your controller object
    #Call your mainloop
    
   

    #while running:
            
       # for event in pygame.event.get():
           # if event.type == pygame.QUIT:
                #running = False
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()
    
