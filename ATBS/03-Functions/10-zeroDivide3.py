# This program also demonstrates Exception handling for a 'Divide by Zero' error.
# Once the execution jumps to the code in the except clause,
# it does not return to the try clause.
# Written in Python 3.5.1 on Mac

def spam(divideBy):
    return 42 / divideBy

try:
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1))
except ZeroDivisionError:
    print('Error: Cannot divide by zero.')
