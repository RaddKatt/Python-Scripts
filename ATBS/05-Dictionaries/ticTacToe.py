"""
This program demonstrates a simple data structure to model a game board for Tic Tac Toe
Written in Python 3.5.1 on Mac
"""

theBoard = {
    'top-L' : ' ',
    'top-M' : ' ',
    'top-R' : ' ',
    'mid-L' : ' ',
    'mid-M' : ' ',
    'mid-R' : ' ',
    'low-L' : ' ',
    'low-M' : ' ',
    'low-R' : ' '
}

def printBoard(board):
    print('\n' + board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'] + '\n')

printBoard(theBoard)
turn = 'X'
for i in range(9):
    move = input('Turn for ' + turn + '. Move on which space? ')
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    printBoard(theBoard)
