my_board = [[1,1,1,1,1],
            [1,0,0,0,1],
            [0,0,0,0,0],
            [2,0,0,0,2],
            [2,2,2,2,2]]
win_condition_1 = [[1,0,0,0,1],
                   [1,1,1,1,1]]
win_condition_2 = [[2,2,2,2,2],
                   [2,0,0,0,2]]
Round = 0
exception = True
game = True
movement = [1,-1
while game:
            Turn = 1
            Round += 1
            print(f"Round: {Round}")
            for i  in range(0,len(my_board)):
            print(my_board[i])
            for t  in range(0,2):
                        print(f"It's player_{Turn} move")
                        while exception:
                                    try:
                                                player = int(input("the placement of the piece in the y-axis (from 0-4): "))
                                                player_piece = int(input("The piece you want (from 0-4): "))
                                                move_y = int(input("y-coordinates: "))
                                                move_x = int(input("x-coordinates: "))
                                                my_board[player + move_y][player_piece + move_x]
                                                my_board[player][player_piece]
                                    except ValueError:
                                                print("Not a valid number; Please Try again")
                                                continueb
                                    except IndexError:
                                                print("Not a valid number; Please Try again")
                                                continue
                                    if my_board[player + move_y][player_piece + move_x] != 0:
                                                print("There is already a piece there; Please Try again")
                                                continue
                                    elif my_board[player][player_piece] != Turn:
                                                 print("This is not your piece or there is no piece in that position; Please Try again")
                                                 continue
                                    elif move_y not in movement or move_x not in movement:
                                                print("You can't move more then one diagonal place from the original position of the piece; Please Try again")
                                                continue
                                    
                                    exception = False
                        my_board[player + move_y][player_piece + move_x] = Turn
                        my_board[player][player_piece] = 0
                        Turn += 1
                        exception = True
                        if Turn == 2:
                                    for i  in range(0,len(my_board)):
                                                print(my_board[i])
                        if win_condition_1[0] ==  my_board[3] and win_condition_1[1] ==  my_board[4]:
                                    Turn = 1
                                    game = False
                                    break

                        elif win_condition_2[0] == my_board[0] and win_condition_2[1] == my_board[1]:
                                    Turn = 2
                                    game = False
                                    break

print(f" Game Over! Congratulation, Player_{Turn} Won !!!! ")


