import pygame as pg

# grid =  [[[2,position],[2,position],[2,position],[2,position],[2,position]],
#             [[2,position],[0,position],[0,position],[0,position],[2,position]],
#             [[0,position],[0,position],[0,position],[0,position],[0,position]],
#             [[1,position],[0,position],[0,position],[0,position],[1,position]],
#             [[1,position],[1,position],[1,position],[1,position],[1,position]]]

       
class Board():
    def __init__(self, blocksize, grid, position, side1, side1_select, side2, side2_select):
        self.blocksize = blocksize
        self.grid = grid
        self.position = position
        self.side1 = side1
        self.side2 = side2
        self.side1_select = side1_select
        self.side2_select = side2_select
    def draw_grid(self, surface, win_condition_1, win_condition_2, Round):
        y_axis = 0
        for y in range(25, 750, self.blocksize):
            x_axis = 0
            for x in range(50, 750, self.blocksize):
                rect = pg.Rect(x, y, self.blocksize, self.blocksize)
                pg.draw.rect(surface, "white", rect, 8)
                self.position = (x + 13,y + 20)
                self.grid[y_axis][x_axis][1] = self.position
                if Round ==0:
                    if  y_axis == 3 or y_axis == 4:
                        win_condition_1[y_axis - 3][x_axis][1] = self.position
                    elif y_axis == 0 or y_axis == 1:
                        win_condition_2[y_axis][x_axis][1] = self.position
                x_axis += 1
            y_axis += 1

    def draw_pieces(self,surface, player_piece_y, player_piece_x):
        for y in range(0,5):
               for x in range(0,5):
                   if self.grid[y][x][0] == 1:
                       if self.grid[y][x] != self.grid[player_piece_y][player_piece_x]:
                           surface.blit(self.side1, self.grid[y][x][1])
                       elif self.grid[y][x] == self.grid[player_piece_y][player_piece_x]:
                           surface.blit(self.side1_select, self.grid[y][x][1])
                   elif self.grid[y][x][0] == 2:
                       if self.grid[y][x] != self.grid[player_piece_y][player_piece_x]:
                            surface.blit(self.side2, self.grid[y][x][1])
                       elif self.grid[y][x] == self.grid[player_piece_y][player_piece_x]:
                            surface.blit(self.side2_select, self.grid[y][x][1])
