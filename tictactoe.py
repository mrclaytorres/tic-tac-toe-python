from functions import *

print('Welcome to Tic Tac Toe!')

while True:
    board = ['|','_','_','_','_','_','_','_','_','_']
    
    display_board(board)

    choose_first()

    player_marker = player_input()
    
    player1 = player_marker[0]
    player2 = player_marker[1]
    
    game_on = True
    
    while True:
        #Player 1 Turn
        
        player_pick1 = player_choice(board)
        
        clear_output()
        
        new_board = place_marker(board, player1, player_pick1)
        
        display_board(new_board)
        
        if win_check(new_board, player1):
            break
        
        if full_board_check(new_board):
            break
        
        
        # Player2's turn.
        
        player_pick2 = player_choice(board)
        
        clear_output()
        
        new_board = place_marker(board, player2, player_pick2)
        
        display_board(new_board)
        
        if win_check(new_board, player2):
            break
        
        if full_board_check(new_board):
            break

    if not replay():
        clear_output()
        break
    else:
        clear_output()
        continue