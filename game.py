import random

def display_board(board):
    print('       |       |     ')
    print('       |       |     ')
    print(f'   {board[7]}   |   {board[8]}   |   {board[9]}')
    print('       |       |     ')
    print('-----------------------')
    print('       |       |     ')
    print(f'   {board[4]}   |   {board[5]}   |   {board[6]}')
    print('       |       |     ')
    print('-----------------------')
    print('       |       |     ')
    print(f'   {board[1]}   |   {board[2]}   |   {board[3]}')
    print('       |       |     ')
    print('       |       |     ')    



def player_input():
    while True:
        player_1=input('Player 1:\nWhich Marker Do You Choose ? (X/O) ').upper()
        player_1.upper()
        if player_1=='X' or player_1=='O':
                return player_1
        else:
            print('wrong marker Choice !! ')



def place_marker(board, marker, position):
    board[position]=marker
    return board



def win_check(board, mark):
    win_condition=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    flag=False
    for a in win_condition:
        for b in a:
            if board[b]==' ' or board[b]!=mark:
                break
        else:
            return True




def choose_first():
    p=randint(2)
    print(f'Player {p} Goes First !!')
    return p



def space_check(board, position):
    return board[position]==' '



def full_board_check(board):
    if ' ' in board:
        return False
    else:
        return True



def player_choice(board):
    while True:
        n=int(input('Enter your position to place your marker '))
        if n in range(1,10):
            if space_check(board,n):
                return n
            else:
                print('The position you have entered is already occupied')
        else:
            replay()



def replay():
    while True:
        s=input('Do You want to play again ?\nYes/No ')
        if s.upper()=='YES':
            return True
        elif s.upper()=='NO':
            return False
        else:
            print('What do you mean ?')



print('Welcome to Tic Tac Toe!')
while True:
    player1=player_input()
    if player1=='X':
        player2='O'
    else:
        player2='X'
    board=['$',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    display_board(board)
    while True:
        print('Player 1:\n')
        position=player_choice(board)
        board=place_marker(board,player1,position)
        print('\n'*100)
        display_board(board)
        if win_check(board,player1):
            print('**Congratulation**\nPlayer 1 WINS !!')
            break;
        if full_board_check(board):
            print('Its a DRAW !!')
            break
        print('Player :2\n')
        position=player_choice(board)
        board=place_marker(board,player2,position)
        print('\n'*100)
        display_board(board)
        if win_check(board,player2):
            print('**Congratulation**\nPlayer 2 WINS !!')
            break;
           
    if not replay():
        break
