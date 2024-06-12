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
            [[0,position],[0,position],[0,position],[0,position],[2,position]],
            [[0,position],[2,position],[0,position],[1,position],[0,position]],
            [[1,position],[0,position],[0,position],[0,position],[0,position]],
            [[1,position],[1,position],[1,position],[1,position],[1,position]]]

win_condition_1 = [[[1,position],[0,position],[0,position],[0,position],[1,position]],
                            [[1,position],[1,position],[1,position],[1,position],[1,position]]]

win_condition_2 = [[[2,position],[2,position],[2,position],[2,position],[2,position]],
                               [[2,position],[0,position],[0,position],[0,position],[2,position]]]

blocksize = 170

player_piece_x = 0
player_piece_y = 0
move_y = 0
move_x = 0
Turn = 1
Round = 0
exception = True
movement = False
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
               if player_piece_y < 4:
                  player_piece_y += 1
                  print(player_piece_y)
            else:
                  pass      
            if event.button == 4:
               if player_piece_y > 0:
                  player_piece_y -= 1
                  print(player_piece_y)
               else:
                  pass
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_1:
                 player_piece_x = 0
                 print(player_piece_x)
            elif event.key == pg.K_2:
                 player_piece_x = 1
                 print(player_piece_x)
            elif event.key == pg.K_3:
                 player_piece_x = 2
                 print(player_piece_x)
            elif event.key == pg.K_4:
                 player_piece_x = 3
                 print(player_piece_x)
            elif event.key == pg.K_d:
                 move_y += 1
                 move_x += 1
                 movement = True
            elif event.key == pg.K_a:
                 move_y += 1
                 move_x -= 1
                 movement = True
            elif event.key == pg.K_q:
                 move_y -= 1
                 move_x -= 1
                 movement = True
            elif event.key == pg.K_e:
                 move_y -= 1
                 move_x += 1
                 movement = True
                   

    # GaRound = 0me logic goes here
    if Turn >= 3:
      Turn = 1
    try:
        grid[player_piece_y + move_y][player_piece_x + move_x][0]
    except IndexError:
        print("Not a valid number; Please Try again")
    if movement:
        if grid[player_piece_y][player_piece_x][0] != Turn:
            print(Turn)
            exception = Falseround
#           print(grid[player_piece_y + move_y][player_piece_x + move_x][0], Turn)
        elif grid[player_piece_y + move_y][player_piece_x + move_x][0] != 0:
            print(grid[player_piece_y + move_y][player_piece_x + move_x])
            print(Turn)
            move_y = 0
            move_x = 0
            exception = False
   
    if movement:
        if exception == True:  
               grid[player_piece_y + move_y][player_piece_x + move_x][0] = Turn
               grid[player_piece_y][player_piece_x][0] = 0
               Turn += 1
               #print(grid[player_piece_y + move_y][player_piece_x + move_x], grid[player_piece_y][player_piece_x])
        exception = True
    if win_condition_1[0] ==  grid[3] and win_condition_1[1] ==  grid[4]:
        Turn = 1
        running = False
       
    elif win_condition_2[0] ==  grid[0] and win_condition_2[1] ==  grid[1]:
        Turn = 2
        running = False
       

               
    # Drawing commands go here
    surface.fill("black")
    board_class.Board(blocksize, grid, position, side1, side2).draw_grid(surface, win_condition_1,
                                                                                                                     win_condition_2, Round)
    board_class.Board(blocksize, grid, position, side1, side2).draw_pieces(surface)
    # Update display, clock, etc.
    pg.display.update()
    if movement:
         move_y = 0
         move_x = 0
         player_piece_y = 0
         player_piece_x = 0
    movement = False
    Round += 1

# Shut down Pygame
pg.quit()
print(f" Game Over! Congratulations, Player_{Turn} Won !!!! ")
