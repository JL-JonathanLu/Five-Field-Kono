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
position = [0,0]
grid =  [[[2,position],[2,position],[2,position],[2,position],[2,position]],
            [[2,position],[0,position],[0,position],[0,position],[2,position]],
            [[0,position],[0,position],[0,position],[0,position],[0,position]],
            [[1,position],[0,position],[0,position],[0,position],[1,position]],
            [[1,position],[1,position],[1,position],[1,position],[1,position]]]

win_condition_1 = [[1,position],[1,position],[1,position],[1,position],[1,position],
                               [1,position],[0,position],[0,position],[0,position],[1,position]]

win_condition_2 = [[2,position],[0,position],[0,position],[0,position],[2,position],
                            [2,position],[2,position],[2,position],[2,position],[2,position]]

blocksize = 170
Turn = 1`
player_piece_x = 0
player_piece_y = 0
move_y = 0 
move_x = 0

# Create a surface for drawing
surface = pg.display.set_mode((surf_width, surf_height))
pg.display.set_caption("My Pygame Program")

# Creating player's pieces
side1 = pg.image.load("images/player_1.png")
side1_rect = side1.get_rect()
side1 = pg.transform.scale(side1, (side1_rect.width * 0.31, side1_rect.height * 0.31))
side1_rect_size = side1.get_size()
side2 = pg.image.load("images/player_2.png")
side2_rect = side2.get_rect()
side2 = pg.transform.scale(side2, (side2_rect.width * 0.31, side2_rect.height * 0.31))
side2_rect_size = side2.get_size()

# MAIN GAME LOOP
running = True
while running:
    # Check event queue for actionable items
    for event in pg.event.get():    
        # Exit the program
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 5:
               if player_piece_y < 5:
                  player_piece_y += 1
            else:
                  pass      
            if event.button == 4:
               if player_piece_y < 0:
                  player_piece_y -= 1
               else:
                  pass
        elif event.type == pg.KEYDOWN:
            elif event.type == pg.k_1:
                 player_piece_x = 0
            elif event.type == pg.k_2:
                 player_piece_x = 1
            elif event.type == pg.k_3:
                 player_piece_x = 2
            elif event.type == pg.k_4:
                 player_piece_x = 3
            elif event.type == pg.k_d:
                 move_y += 1 
                 move_x += 1  
            elif event.type == pg.k_s:
                 move_y += 1 
                 move_x -= 1
            elif event.type == pg.k_w:
                 move_y -= 1 
                 move_x -= 1
            elif event.type == pg.k_e:
                 move_y -= 1 
                 move_x += 1
                   

    # Game logic goes here
    if Turn >= 3:
       Turn = 1     
    while exception:
          try:
               grid[player_piece_y + move_y][player_piece_x + move_x] 
               except IndexError:
                       print("Not a valid number; Please Try again")
                       continue
               if grid[player_piece_y + move_y][player_piece_x + move_x] != 0:
                        print("There is already a piece there; Please Try again")
                        continue
               elif grid[player_piece_y][player_piece_x] != Turn:
                        print("This is not your piece or there is no piece in that position; Please Try again")
                        continue
                        
            exception = False

    if exception == False:  
           grid[player_piece_y + move_y][player_piece_x + move_x][0] = Turn
           grid[player_piece_y][player_piece_x] = 0
           Turn += 1
           exception = True 
                
    # Drawing commands go here
    board_class.Board(blocksize, grid, position, side1, side2).draw_grid(surface)
    # Update display, clock, etc.
    pg.display.update()

# Shut down Pygame
pg.quit()


