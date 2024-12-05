import pygame
from src import cell

class Maze:
    
    def __init__(self, rows, cols, screen, size, border):
        self.row = rows
        self.col = cols
        self.screen = screen
        self.color = 'blue'
        self.bord_col = border
        self.size = size
        self.dir = 90
        self.list = []
        
    def drawGrid(self):   
        
        num = 1
        grid_size = int((self.screen.get_height() - (2 * self.size)))
        for x in range(0, self.screen.get_width(), self.size):
            for y in range(0, grid_size, self.size):
                box = cell.Cell(x, y, self.screen, False, num, self.size)
                num += 1
                self.list.append(box)
                box.draw()
                box.get_num()
                
                
                
                
                
                
       # current_x = 0
        #current_y = 0
        #box = cell.Cell(current_x, current_y, self.screen, True)
        #box.draw(self.size)
    
            
            
        