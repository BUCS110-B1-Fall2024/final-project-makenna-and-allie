import pygame
from src import controller
#import your controller

def main():
    pygame.init()
    control = controller.Controller()
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
