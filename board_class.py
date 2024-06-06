import pygame as pg

class GamePiece:
    def __init__(self, player1 = [], player2 = []):
        self.player1 = player1
        self.player2 = player2
    def draw_piece(self, surface, y_axis, x_axis, sprite_group1, sprite_group2):        
        if y_axis == 0:
            surface.blit(self.side1, (self.position[x_axis][0], self.position[x_axis][1]))
            sprite_group1.add(self.side1)
        elif y_axis == 1:
            if x_axis == 0 or x_axis == 4:
                surface.blit(self.side1, (self.position[x_axis][0], self.position[x_axis][1]))
                sprite_group1.add(self.side1)
        elif y_axis == 3:
            if x_axis == 0 or x_axis == 4:
                surface.blit(self.side2, (self.position[x_axis][0], self.position[x_axis][1]))
                sprite_group2.add(self.side2)
        elif y_axis == 4:
            surface.blit(self.side2, (self.position[x_axis][0], self.position[x_axis][1]))
            sprite_group2.add(self.side2)
       
class Board(GamePiece):
    def __init__(self, blocksize, grid, position, side1, side2, sprite_group1, sprite_group2):
        self.blocksize = blocksize
        self.grid = grid
        self.position = position
        self.side1 = side1
        self.side2 = side2
        self.sprite_group1 = sprite_group1
        self.sprite_group2 = sprite_group2
    def draw_grid(self, surface):
        y_axis = 0
        for y in range(25, 750, self.blocksize):
            self.position = []
            x_axis = 0
            for x in range(50, 750, self.blocksize):
                rect = pg.Rect(x, y, self.blocksize, self.blocksize)
                pg.draw.rect(surface, "white", rect, 8)
                self.position.append((x + 13,y + 20))
                GamePiece.draw_piece(self, surface, y_axis, x_axis, self.sprite_group1, self.sprite_group2)
                x_axis += 1
            self.grid.append(self.position)
            y_axis += 1
    def turns(self):
        turn = 0
        move_x, move_y = 0, 0



