# Imported pygame module and python file containing classes to program the game board
import pygame as pg
import board_class
pg.init()

# Variables containing pygame window size
surf_width, surf_height = 950, 900

# Variable containing grid layout and positions on the pygame window
position = [0,0]
grid =  [[[2,position],[2,position],[2,position],[2,position],[2,position]],
            [[2,position],[0,position],[0,position],[0,position],[2,position]],
            [[0,position],[0,position],[0,position],[1,position],[0,position]],
            [[1,position],[0,position],[0,position],[0,position],[0,position]],
            [[1,position],[1,position],[1,position],[1,position],[1,position]]]


# Conditions to end the game
win_condition_1 = [[[1,position],[0,position],[0,position],[0,position],[1,position]],
                    [[1,position],[1,position],[1,position],[1,position],[1,position]]]

win_condition_2 = [[[2,position],[2,position],[2,position],[2,position],[2,position]],
                    [[2,position],[0,position],[0,position],[0,position],[2,position]]]

# Varibles used in the class file
blocksize = 170
player_piece_x = 0
player_piece_y = 0
move_y = 0
move_x = 0

# Variables used in the game loop
Turn = 1
Round = 0
exception = True
movement = False
game = "on"

# Create a surface for drawing
surface = pg.display.set_mode((surf_width, surf_height))
pg.display.set_caption("Five Field Kono")

# Creating player's pieces
side1 = pg.image.load("images/player_1.png")
side1_rect = side1.get_rect()
side1 = pg.transform.scale(side1, (side1_rect.width * 0.31, side1_rect.height * 0.31))
side1_rect_size = side1.get_size()
side2 = pg.image.load("images/player_2.png")
side2_rect = side2.get_rect()
side2 = pg.transform.scale(side2, (side2_rect.width * 0.31, side2_rect.height * 0.31))
side2_rect_size = side2.get_size()

#Creates a separate player piece to highlight current piece selected
side1_select = pg.image.load("images/player_1_select.png")
side1_select_rect = side1_select.get_rect()
side1_select = pg.transform.scale(side1_select, (side1_select_rect.width * 0.31, side1_select_rect.height * 0.31))
side1_select_rect_size = side1_select.get_size()
side2_select = pg.image.load("images/player_2_select.png")
side2_select_rect = side2_select.get_rect()
side2_select = pg.transform.scale(side2_select, (side2_select_rect.width * 0.31, side2_select_rect.height * 0.31))
side2_select_rect_size = side2_select.get_size()

# load a font
header_size = pg.font.Font("fonts/MUSASHI.ttf", 100)
main_text_size = pg.font.Font("fonts/Doctor Glitch.otf", 50)
end_text_size = pg.font.Font("fonts/MUSASHI.ttf", 60)
intro_text = main_text_size.render("Start", True, "black")
name_text = header_size.render(f"Five Field Kono", True, "gold")
replay_text = main_text_size.render("Play again?", True, "red")

# MAIN GAME LOOP
running = True
while running:
    # Check event queue for actionable items
    for event in pg.event.get():    
        # Exit the program
        if event.type == pg.QUIT:
            running = False
        # selecting a player's pieces    
        # selecting a row
        # Left mouse button clicks (mouse button 1) are used for screen transitions from title screen and game end screen
        # Scroll wheel (mouse button 4 and 5) selects grid row   
        if game == "on" or game == "end":
            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if game == "on":
                        game = "start"
                    elif game == "end":
                        game = "start"
        if game == "start":
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 5:
                   if player_piece_y < 4:
                      player_piece_y += 1
                      print(f"Row {player_piece_y}")
                else:
                      pass      
                if event.button == 4:
                   if player_piece_y > 0:
                      player_piece_y -= 1
                      print(f"Row {player_piece_y}")
                   else:
                      pass                  
            elif event.type == pg.KEYDOWN:
                # selecting a column        
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
                elif event.key == pg.K_5:
                     player_piece_x = 4
                     print(player_piece_x)
                # movement option for the player
                # d key moves piece down and right
                # a key moves piece down and left
                # q key moves piece up and left
                # e key moves piece up and right
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
                   

    # Turn system
    # Turn resets to 1 after turn 2, turn 1 represents player 1 and turn 2 represents player 2
    if Turn >= 3:
      Turn = 1
    # exception and checks to stop player from breaking the rule            
    try:
        grid[player_piece_y + move_y][player_piece_x + move_x][0]
    # exception to checks if the player movement is out of the board 
    except IndexError:
        exception = False
    # See if the player make a move then go though three different checks
    # The first check is to see if the player is moving their own pieces
    # The second check is to see if the position the player is moving to is a empty space or not
    # The third check is to see if the moving piece is going to teleport across the board  
    if movement:
        if grid[player_piece_y][player_piece_x][0] != Turn:
            print(Turn)
            exception = False
        elif grid[player_piece_y + move_y][player_piece_x + move_x][0] != 0:
            move_y = 0
            move_x = 0
            exception = False
        elif -1 in grid[player_piece_y + move_y][player_piece_x + move_x][1]:
            print(grid[player_piece_y + move_y][player_piece_x + move_x][1])
            move_y = 0
            move_x = 0
            exception = False        
   
    if movement:
        if exception:  
               grid[player_piece_y + move_y][player_piece_x + move_x][0] = Turn
               grid[player_piece_y][player_piece_x][0] = 0
               Turn += 1
               #print(grid[player_piece_y + move_y][player_piece_x + move_x], grid[player_piece_y][player_piece_x])
        exception = True

# Compares current grid to the victory condtions
# If the grid matches the win condition, the game ends and determines the winner based on the win condition matched
    if game == "start":
        if win_condition_1[0][0] == grid[3][0] and win_condition_1[0][4] ==  grid[3][4] and win_condition_1[1] == grid[4]:
            Turn = 1
            print(game)
            game = "end"
               
        elif win_condition_2[0] == grid[0] and win_condition_2[1][0] == grid[1][0] and win_condition_2[1][4] == grid[1][4]:
            Turn = 2
            game = "end"              
               
    # Drawing commands
    # break the game up into three different phase
    # The intro screen, when game == "on"
    # When the game is playing, when game == "start"
    # When there is a winner and the game end, when game == "end"           
    if game == "on":
       surface.fill("white")
       surface.blit(name_text, (130,300 ))
       surface.blit(intro_text, (375,500 ))
    elif game == "start":
       surface.fill("black")
       board_class.Board(blocksize, grid, position, side1, side1_select,
                                        side2, side2_select).draw_grid(surface, win_condition_1,
                                                                        win_condition_2, Round,)
       
       board_class.Board(blocksize, grid, position, side1, side1_select,
                                      side2, side2_select).draw_pieces(surface, player_piece_y, player_piece_x)
    elif game == "end":
       print(Turn)
       win_text = end_text_size.render(f"Congratulations, Player_{Turn} Won !!!!", True, "gold")
       surface.fill("black")
       surface.blit(win_text, (25, 400))
       surface.blit(replay_text, (300, 500))
    
    # Updates game display and resets movement for the next player's turn
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

