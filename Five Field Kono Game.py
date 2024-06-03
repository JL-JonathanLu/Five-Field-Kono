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
# Create a surface for drawing
surface = pg.display.set_mode((surf_width, surf_height))
pg.display.set_caption("My Pygame Program")

# MAIN GAME LOOP
running = True
while running:
    # Check event queue for actionable items
    for event in pg.event.get():    
        # Exit the program
        if event.type == pg.QUIT:
            running = False
#         elif event.type == pg.MOUSEBUTTONDOWN:
#             if event.button == 1:
                
                    

    # Game logic goes here
    
    # Drawing commands go here
    board_class.Board(170).draw(surface)
    board_class.Game_Piece((50, 140, 25)).draw(surface)
    # Update display, clock, etc.
    pg.display.update()

# Shut down Pygame
pg.quit()
