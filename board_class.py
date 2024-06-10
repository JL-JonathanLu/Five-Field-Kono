import pygame as pg

# grid =  [[[2,position],[2,position],[2,position],[2,position],[2,position]],
#             [[2,position],[0,position],[0,position],[0,position],[2,position]],
#             [[0,position],[0,position],[0,position],[0,position],[0,position]],
#             [[1,position],[0,position],[0,position],[0,position],[1,position]],
#             [[1,position],[1,position],[1,position],[1,position],[1,position]]]

       
class Board():
    def __init__(self, blocksize, grid, position, side1, side2):
        self.blocksize = blocksize
        self.grid = grid
        self.position = position
        self.side1 = side1
        self.side2 = side2
    def draw_grid(self, surface):
        y_axis = 0
        for y in range(25, 750, self.blocksize):
            x_axis = 0
            for x in range(50, 750, self.blocksize):
                rect = pg.Rect(x, y, self.blocksize, self.blocksize)
                pg.draw.rect(surface, "white", rect, 8)
                self.position = (x + 13,y + 20)
                self.grid[y_axis][x_axis][1] = self.position
                x_axis += 1
            y_axis += 1

    def draw_pieces(self,surface):
        for y in range(0,5):
               for x in range(0,5):
                   if self.grid[y][x][0] == 1:
                        surface.blit(self.side1, self.grid[y][x][1])
                   elif self.grid[y][x][0] == 2:
                        surface.blit(self.side2, self.grid[y][x][1])
                        
    
               
           
 



