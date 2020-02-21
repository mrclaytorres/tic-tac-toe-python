import random

def display_board(board): #Print the board
    border = ''
    for input in board:
        if input == '|':
            border = input
    return print(f'{board[7]} {border} {board[8]} {border} {board[9]}\n----------\n{board[4]} {border} {board[5]} {border} {board[6]}\n----------\n{board[1]} {border} {board[2]} {border} {board[3]}')


def player_input():

    while True:

        player1 = input("Please pick a marker 'X' or 'O'")
        if player1.lower() not in ('x', 'o'):
            print("Not an appropriate choice.")
        else:
            break

    if player1.lower() == 'x':
        player2 = 'O'
    else:
        player2 = 'X'

    return player1.upper(), player2.upper()


def place_marker(board, marker, position): #Player places a marker
    board[position] = marker.upper()
    return board

def win_check(board, mark): #Check if the Player move is a win move
    for tile in board:
        if ''.join(board[1:4]) == mark*3:
            print(f'{mark} won!')
            return True
        elif ''.join(board[4:7]) == mark*3:
            print(f'{mark} won!')
            return True
        elif ''.join(board[7:]) == mark*3:
            print(f'{mark} won!')
            return True
        elif ''.join(board[1:8:3]) == mark*3:
            print(f'{mark} won!')
            return True
        elif ''.join(board[2:9:3]) == mark*3:
            print(f'{mark} won!')
            return True
        elif ''.join(board[3::3]) == mark*3:
            print(f'{mark} won!')
            return True
        elif ''.join(board[3:8:2]) == mark*3:
            print(f'{mark} won!')
            return True
        elif ''.join(board[1::4]) == mark*3:
            print(f'{mark} won!')
            return True
        else:
            break

def choose_first(): #Randomize which player picks first
    random_num = random.randint(1,2)
    if random_num == 1:
        return print(f'Player 1 will pick first')
    else:
        return print(f'Player 2 will pick first')

def space_check(board, position): #Check if the position in empty
    if board[position] == "_":
        return True
    else:
        return print(f'Cell in not empty.')

def full_board_check(board): #Check if the board is full
    for space in board:
        if "_" in ''.join(board):
            return False
        else:
            print(f"It's a draw!")
            return True

def player_choice(board): #Take the players next move
    while True:
        position = int(input('Next player move (Choose between 1-9)'))
        if str(position) not in ('123456789'):
            print("Not an appropriate choice.")
            
        elif space_check(board, position):
            return position
        else:
            continue
    

def replay(): #Check if the player wants to play again
    play_again = ''
    while True:
        play_again = input('Do you want to play again? Yes or No')
        if play_again.lower() not in ('yes', 'no'):
            print("Not an appropriate choice.")
        elif play_again.lower() == 'yes':
            return True
        else:
            break
            
def clear_output():
    print('\n'*100)