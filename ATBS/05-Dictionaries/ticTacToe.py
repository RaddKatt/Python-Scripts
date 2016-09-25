"""
This program demonstrates a simple data structure to model a game board for Tic Tac Toe
Written in Python 3.5.1 on Mac
"""

theBoard = {
    1 : ' ',
    2 : ' ',
    3 : ' ',
    4 : ' ',
    5 : ' ',
    6 : ' ',
    7 : ' ',
    8 : ' ',
    9 : ' '
}

turn = 'X'

def printBoard(board):
    print('\n' + board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9] + '\n')

def checkMove(move):
    while True:
        errMsg = 'Move entered must be a number between 1 and 9.'
        try:
            move = int(move)            # if move is an integer
            if move < 1 or move > 9:    # if move is lt 1 or gt 9
                print(errMsg)
                move = input(prompt)
                continue
            elif theBoard[move] != ' ': # if space is already taken
                move = (input('Space ' + str(move) + ' is already taken. Try again: '))
                continue
            else:
                return move
        except:                         # if move is not an integer
            print(errMsg)
            move = input(prompt)
            continue

'''
def checkWin(board):
    if
    break
'''

for i in range(9):
    # checkWin(board)
    prompt = 'Turn for ' + turn + '. Move on which space? (1-9) '
    printBoard(theBoard)
    move = input(prompt)
    move = checkMove(move)

    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
