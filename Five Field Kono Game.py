# ===========================================================================
# PYGAME TEMPLATE
# Use this as a starting point for your Pygame projects.
# ===========================================================================

# Imported modules and initialization (add as necessary)
import pygame as pg
import board_class
pg.init()

# Define constants (add as necessary)
surf_width, surf_height = 950, 900
grid = []
position = []
blocksize = 170

# Create a surface for drawing
surface = pg.display.set_mode((surf_width, surf_height))
pg.display.set_caption("My Pygame Program")

# Creating player's pieces 
side1 = pg.image.load("images/player_1.png")
side1_rect = side1.get_rect()
side1 = pg.transform.scale(side1, (side1_rect.width * 0.31, side1_rect.height * 0.31))
side1_rect.size = side1.get_size()
side2 = pg.image.load("images/player_2.png")
side2_rect = side2.get_rect()
side2 = pg.transform.scale(side2, (side2_rect.width * 0.31, side2_rect.height * 0.31))
side2_rect.size = side2.get_size()
sprite_group1 = pg.sprite.Group
sprite_group2 = pg.sprite.Group

# MAIN GAME LOOP
running = True
while running:
    # Check event queue for actionable items
    for event in pg.event.get():    
        # Exit the program
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse = pg.mouse.get_pos()
                for i in sprite_group1:
                    if side1_rect.collidepoint(mouse):
                        print("click")
               
                   

    # Game logic goes here
   
    # Drawing commands go here
    p1 = board_class.GamePiece()
    board_class.Board(blocksize, grid, position, side1, side2, sprite_group1, sprite_group2).draw_grid(surface)
    # Update display, clock, etc.
    pg.display.update()

# Shut down Pygame
pg.quit()
