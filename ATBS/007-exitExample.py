# This program demonstrates ending a program with 'sys.exit()'
# Written in Python 3.5.1

import sys

while True:
    response = input('Type \'exit\' to exit: ')
    if response == 'exit':
        print('Goodbye.')
        sys.exit()
    print('You typed: ' + response + '.')
