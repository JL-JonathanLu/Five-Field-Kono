class Board:
    def __init__(self, blocksize, position = []):
        self.blocksize = blocksize
        self.position = position
    def draw(self, surface):
        for x in range(50, 750, self.blocksize):
            for y in range(25, 750, self.blocksize):
                rect = pg.Rect(x, y, self.blocksize, self.blocksize)
                self.position.append((x,y))
                pg.draw.rect(surface, "white", rect, 8)
       

class Game_Piece:
    def __init__(self, colour = ()):
        self.colour = colour
    def draw(self, surface):
        image = pg.draw.circle(surface, self.colour, (55, 790), 5)
        image_y //= 2

