#Creator Shubhendu Nath
#Created on 1st June,2020

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
    while marker!='X' and marker!='O':
        marker=input("Choose X or O: ").upper()
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

def defend_move(board,marker):
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

def attack_move(board,marker):
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

def arbitary_move(board):
    while True:
        x=random.randint(1,9)
        if space_check(board,x):
            break
    return x

def smart_move(board):
    while True:
        lst=[1,3,7,9]
        x=random.sample(lst,1)
        value=x[0]
        if space_check(board,value):
            break
    return value

def winning_move(board,marker):
    total=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[7,5,3]]
    sample=[]
    for i in total:
        count=0
        for j in i:
            if space_check(board,j) or board[j]==marker:
                count+=1
                continue
        if count==3:
            sample.append(i)
    x=set(sample[0]).intersection(set(sample[1]))
    return list(x)[0]



print("Welcome to Tic Tac Toe")

while True:
    the_board=[' ']*10
    move_player=0
    move_CPU=0
    player_1_marker,CPU_marker=player_input()
    turn=choose_first()
    print(turn+" will go first")
    first_turn=turn
    play_game=input("Ready to play? y or n? ")
    if play_game=='y':
        game_on=True
        level=input('Enter Level(Easy[e]/Medium[m]/Hard[h]): ').upper()
    else:
        game_on=False
    while game_on:
        if turn=='Player_1':
            display_board(the_board)
            position=player_choice(the_board)
            place_marker(the_board,player_1_marker,position)
            move_player+=1
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
            if(level=='E'):
                display_board(the_board)
                auto_position=arbitary_move(the_board)
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
            elif(level=='M'):
                display_board(the_board)
                if empty_board(the_board)==True:
                    while True:
                        x=random.randint(1,9)
                        if x%2!=0:
                            place_marker(the_board,CPU_marker,x)
                            break
                else:
                    if attack_move(the_board,CPU_marker)!= -1:
                        auto_position=attack_move(the_board,CPU_marker)
                        place_marker(the_board,CPU_marker,auto_position)

                    elif defend_move(the_board,player_1_marker)!= -1:
                        auto_position=defend_move(the_board,player_1_marker)
                        place_marker(the_board,CPU_marker,auto_position)
                    else:
                        auto_position=arbitary_move(the_board)
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
            else:
                if first_turn=='Player_1':
                    display_board(the_board)
                    if move_player==1:
                        if the_board[5] == player_1_marker:
                            lst=[1,3,7,9]
                            x=random.sample(lst,1)
                            auto_position=x[0]
                            place_marker(the_board,CPU_marker,auto_position)
                            move_CPU+=1
                        else:
                            place_marker(the_board,CPU_marker,5)
                            move_CPU+=1
                    else:
                        if attack_move(the_board,CPU_marker)!= -1:
                            auto_position=attack_move(the_board,CPU_marker)
                            place_marker(the_board,CPU_marker,auto_position)
                            move_CPU+=1
                        elif defend_move(the_board,player_1_marker)!= -1:
                            auto_position=defend_move(the_board,player_1_marker)
                            place_marker(the_board,CPU_marker,auto_position)
                            move_CPU+=1
                        else:
                            auto_position=smart_move(the_board)
                            place_marker(the_board,CPU_marker,auto_position)
                            move_CPU+=1
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
                else:
                    display_board(the_board)
                    if empty_board(the_board):
                        lst=[1,3,5,7,9]
                        x=random.sample(lst,1)
                        value=x[0]
                        place_marker(the_board,CPU_marker,value)
                        move_CPU+=1
                    elif move_CPU==1:
                        if the_board[5]==CPU_marker:
                            for i in range (1,10):
                                if the_board[i]==player_1_marker:
                                    player_position=i
                                    break
                            if player_position in [1,3,7,9]:
                                CPU_position=10-player_position
                                place_marker(the_board,CPU_marker,CPU_position)
                                move_CPU+=1
                            else:
                                if player_position==2:
                                    lst=[7,9]
                                    x=random.sample(lst,1)
                                    value=x[0]
                                    place_marker(the_board,CPU_marker,value)
                                    move_CPU+=1
                                elif player_position==4:
                                    lst=[3,9]
                                    x=random.sample(lst,1)
                                    value=x[0]
                                    place_marker(the_board,CPU_marker,value)
                                    move_CPU+=1
                                elif player_position==6:
                                    lst=[1,7]
                                    x=random.sample(lst,1)
                                    value=x[0]
                                    place_marker(the_board,CPU_marker,value)
                                    move_CPU+=1
                                elif player_position==8:
                                    lst=[1,3]
                                    x=random.sample(lst,1)
                                    value=x[0]
                                    place_marker(the_board,CPU_marker,value)
                                    move_CPU+=1
                        else:
                            for i in range (1,10):
                                if the_board[i]==player_1_marker:
                                    player_position=i
                                    break
                            if player_position%2==0:
                                place_marker(the_board,CPU_marker,5)
                                move_CPU+=1
                            else:
                                if player_position==5:
                                    for i in range (1,10):
                                        if the_board[i]==CPU_marker:
                                            CPU_prev_position=i
                                            break
                                    CPU_position=10-CPU_prev_position
                                    place_marker(the_board,CPU_marker,CPU_position)
                                    move_CPU+=1
                                else:
                                    auto_position=winning_move(the_board,CPU_marker)
                                    place_marker(the_board,CPU_marker,auto_position)
                                    move_CPU+=1
                    else:
                        if attack_move(the_board,CPU_marker)!= -1:
                            auto_position=attack_move(the_board,CPU_marker)
                            place_marker(the_board,CPU_marker,auto_position)
                            move_CPU+=1
                        elif defend_move(the_board,player_1_marker)!= -1:
                            auto_position=defend_move(the_board,player_1_marker)
                            place_marker(the_board,CPU_marker,auto_position)
                            move_CPU+=1
                        else:
                            try:
                                auto_position=winning_move(the_board,CPU_marker)
                                place_marker(the_board,CPU_marker,auto_position)
                                move_CPU+=1
                            except:
                                auto_position=arbitary_move(the_board)
                                place_marker(the_board,CPU_marker,auto_position)
                                move_CPU+=1
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
