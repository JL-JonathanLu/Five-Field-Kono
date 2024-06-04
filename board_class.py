class Board:
    def __init__(self, blocksize, grid = []):
        self.blocksize = blocksize
        self.grid = grid
    def draw(self, surface):
        x_axi = 0
        for x in range(50, 750, self.blocksize):
            position = []
            y_axi = 0
            for y in range(25, 750, self.blocksize):
                rect = pg.Rect(x, y, self.blocksize, self.blocksize)
                pg.draw.rect(surface, "white", rect, 8)
                position.append((x,y))
                y_axi += 1
            self.grid.append(position)
            x_axi += 1
       

class Game_Piece:
    def __init__(self, colour = ()):
        self.colour = colour
    def draw(self, surface):
        image = pg.draw.circle(surface, self.colour, (55, 790), 5)
        image_y //= 2

