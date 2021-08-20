from IPython.display import clear_output
import random

def display_board(board):

    clear_output()
    print(board[1]+'|'+board[2]+'|'+board[3])
    print("-----")
    print(board[4]+'|'+board[5]+'|'+board[6])
    print("-----")
    print(board[7]+'|'+board[8]+'|'+board[9])
    print("-----")


def player_input():

    marker=''
    name=input("Enter Your Name: ")
    print(name,"Choose X or O: ")
    while marker!='X' and marker!='O':
        marker=input().upper()
    if marker=='X':
        return ('X','O')
    else:
        return ('O','X')


def place_marker(board,marker,position):

    board[position]=marker


def win_check(board,marker):

    return ((board[1]==board[2]==board[3]==marker) or (board[4]==board[5]==board[6]==marker) or (board[7]==board[8]==board[9]==marker) or (board[1]==board[4]==board[7]==marker) or (board[2]==board[5]==board[8]==marker) or (board[3]==board[6]==board[9]==marker) or (board[1]==board[5]==board[9]==marker) or (board[3]==board[5]==board[7]==marker))


def choose_first():

    flip=random.randint(0,1)
    if flip==1:
        return 'Player_1'
    else:
        return 'CPU'


def space_check(board,position):

    return board[position]==' '


def full_board_check(board):

    for i in range(1,10):
        if space_check(board,i):
            return False
    return True


def player_choice(board):

    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position=int(input("Choose a position between 1 to 9 : "))
    return position


def replay():

    return input("Do you want to play again:Yes or No: ").lower().startswith('y')


def empty_board(board):

    for i in range (1,10):
        if space_check(board,i):
            continue
        else:
            break
    if i==9:
        return True
    else:
        return False


def position_check(board,marker):
    if (board[3]==board[2]==marker and board[1]==' ') or (board[9]==board[5]==marker and board[1]==' ') or (board[7]==board[4]==marker and board[1]==' '):
        return 1
    elif (board[3]==board[1]==marker and board[2]==' ') or (board[8]==board[5]==marker and board[2]==' '):
        return 2
    elif (board[1]==board[2]==marker and board[3]==' ') or (board[9]==board[6]==marker and board[3]==' ') or (board[7]==board[5]==marker and board[3]==' '):
        return 3
    elif (board[7]==board[1]==marker and board[4]==' ') or (board[6]==board[5]==marker and board[4]==' '):
        return 4
    elif (board[6]==board[4]==marker and board[5]==' ') or (board[8]==board[2]==marker and board[5]==' ') or (board[7]==board[3]==marker and board[5]==' ') or (board[9]==board[1]==marker and board[5]==' '):
        return 5
    elif (board[2]==board[4]==marker and board[6]==' ') or (board[3]==board[9]==marker and board[6]==' '):
        return 6
    elif (board[1]==board[4]==marker and board[7]==' ') or (board[9]==board[8]==marker and board[7]==' ') or (board[3]==board[5]==marker and board[7]==' '):
        return 7
    elif (board[2]==board[5]==marker and board[8]==' ') or (board[9]==board[7]==marker and board[8]==' '):
        return 8
    elif (board[1]==board[5]==marker and board[9]==' ') or (board[7]==board[8]==marker and board[9]==' ') or (board[3]==board[6]==marker and board[9]==' '):
        return 9
    else:
        return -1


def arbitary_position(board):
    while True:
        x=random.randint(1,9)
        if space_check(board,x):
            break
    return x


import random
print("Welcome to Tic Tac Toe")

while True:
    the_board=[' ']*10
    player_1_marker,CPU_marker=player_input()
    turn=choose_first()
    print(turn+" will go first")
    play_game=input("Ready to play? y or n? ")
    if play_game=='y':
        game_on=True
    else:
        game_on=False
    while game_on:
        if turn=='Player_1':
            display_board(the_board)
            position=player_choice(the_board)
            place_marker(the_board,player_1_marker,position)
            if win_check(the_board,player_1_marker)==True:
                display_board(the_board)
                print("Player 1 has won")
                game_on=False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("The game is a tie")
                    game_on=False
                else:
                    turn='CPU'
        else:
            display_board(the_board)
            if empty_board(the_board)==True:
                while True:
                    x=random.randint(1,9)
                    if x%2!=0:
                        place_marker(the_board,CPU_marker,x)
                        break
            else:
                if position_check(the_board,player_1_marker)==True:
                    auto_position=position_check(the_board,player_1_marker)
                    place_marker(the_board,CPU_marker,auto_position)
                else:
                    auto_position=arbitary_position(the_board)
                    place_marker(the_board,CPU_marker,auto_position)
            if win_check(the_board,CPU_marker)==True:
                display_board(the_board)
                print("CPU has won")
                game_on=False
            else:
                if full_board_check(the_board)==True:
                    display_board(the_board)
                    print("The game is a tie")
                    game_on=False
                else:
                    turn='Player_1'
    if not replay():
        break
