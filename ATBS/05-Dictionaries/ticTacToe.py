"""
This program demonstrates a simple data structure to model a game board for Tic Tac Toe
Written in Python 3.5.1 on Mac
"""

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

def printBoard(board):
    print('\n' + board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'] + '\n')

'''
def checkWin(board):
    if
    break
'''

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
