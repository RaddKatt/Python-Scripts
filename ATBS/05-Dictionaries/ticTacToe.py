"""
This program demonstrates a simple data structure to model a game board for Tic Tac Toe
Written in Python 3.5.1 on Mac
"""

import string

theBoard = {
    '1' : ' ',
    '2' : ' ',
    '3' : ' ',
    '4' : ' ',
    '5' : ' ',
    '6' : ' ',
    '7' : ' ',
    '8' : ' ',
    '9' : ' '
}

turn = 'X'

def printBoard(board):
    print('\n' + board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'] + '\n')

def checkMove(move):
    while True:
        errMsg = 'Move entered must be a number between 1 and 9.'
        if not move.isnumeric():
            print(errMsg)
            move = input(prompt)
            continue
        elif int(move) < 1 or int(move) > 9:
            print(errMsg)
            move = input(prompt)
            continue
        else:
            return move

'''
def checkWin(board):
    if
    break
'''

for i in range(9):
    prompt = 'Turn for ' + turn + '. Move on which space? (1-9) '
    printBoard(theBoard)
    move = input(prompt)
    move = checkMove(move)

    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
