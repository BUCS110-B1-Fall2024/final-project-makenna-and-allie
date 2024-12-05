import pygame



from Button import Button



class Setup:
    
    def __init__(self, color):
        self.size = 1200
        self.color = color
        
    def create(self):
        
        pygame.init()
        
        #screen = pygame.display.set_mode((pygame.display.Info().current_w, pygame.display.Info().current_h),pygame.FULLSCREEN)
        
        screen = pygame.display.set_mode((1200,1200))
        pygame.display.set_caption('Maze')
        #screen.fill(self.color)
        
        pygame.display.flip()

        button1 = button.Button(50, 30, 1100, 400, 'blue', screen, "konecheewa", 'black', 5)
        button1.draw()
        
        pygame.display.flip()

        button2 = button.Button(50, 450, 545, 200, 'grey', screen, "hola", 'black', 5)
        
        button2.draw()

        pygame.display.flip()

        button3 = button.Button(605, 450, 182, 200, 'white', screen, "Easy", "white", 5)
        button4 = button.Button(787, 450, 182, 200, 'white', screen, "Medium", "white", 5)
        button5 = button.Button(968, 450, 182, 200, 'white', screen, "Hard", "white", 5)
        button3.draw()
        button4.draw()
        button5.draw()

        pygame.display.flip()
        
        running = True 

        while running:
                
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    key=pygame.key.name(event.key)
                    print(key)
                    screen.fill('black')
                if event.type == pygame.QUIT:
                    running = False
                    