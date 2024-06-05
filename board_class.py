import pygame as pg

class GamePiece:
    def draw_piece(self, surface, y_axis, x_axis):
        print(self.position)
        if y_axis == 0:
            pg.draw.circle(surface, "red", (self.position[x_axis][0] + 85, self.position[x_axis][1]+80), 60)
        elif y_axis == 1:
            if x_axis == 0 or x_axis == 4:
                pg.draw.circle(surface, "red", (self.position[x_axis][0]+85 , self.position[x_axis][1]+80), 60)
        elif y_axis == 3:
            if x_axis == 0 or x_axis == 4:
                pg.draw.circle(surface, "blue", (self.position[x_axis][0]+85 , self.position[x_axis][1]+80), 60)
        elif y_axis == 4:
            pg.draw.circle(surface, "blue", (self.position[x_axis][0] + 85, self.position[x_axis][1]+80), 60)
        
class Board(GamePiece):
    def __init__(self, blocksize = 170 , grid = [], position = []):
        self.blocksize = blocksize
        self.grid = grid
        self.position = position
    def draw_grid(self, surface):
        y_axis = 0
        for y in range(25, 750, self.blocksize):
            self.position = []
            x_axis = 0
            for x in range(50, 750, self.blocksize):
                rect = pg.Rect(x, y, self.blocksize, self.blocksize)
                pg.draw.rect(surface, "white", rect, 8)
                self.position.append((x,y))
                GamePiece.draw_piece(self, surface, y_axis, x_axis)
                x_axis += 1
            self.grid.append(self.position)
            y_axis += 1

#         # check if the self.grid
#         for i  in range(0,len(self.grid)):
#             print(self.grid[i])



