import pygame
import Setup
#import your controller

def main():
    pygame.init()
    #Create an instance on your controller object
    #Call your mainloop
    begin = Setup.Setup("grey")
    begin.create()
    
    running = True 

    while running:
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()
