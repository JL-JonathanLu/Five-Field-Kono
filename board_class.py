import pygame as pg
import random

class Board:
    def __init__(self, blocksize):
        self.blocksize = blocksize
    def draw(self, surface):
        for x in range(50, 750, self.blocksize):
            for y in range(25, 750, self.blocksize):
                rect = pg.Rect(x, y, self.blocksize, self.blocksize)
                pg.draw.rect(surface, "white", rect, 8)

class Game_Piece:
    def __init__(self, colour = ()):
        self.colour = colour
    def draw(self, surface):
        pg.draw.circle(surface, self.colour, (55, 705), 5)
        image = pg.draw.circle(surface, self.colour, (55, 705), 5)
        image_x,image_y = image.get_rect()
        image_x //= 2
        image_y //= 2

