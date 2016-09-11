# This program demonstrates Exception handling for a 'Divide by Zero' error.
# Written in Python 3.5.1

def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Cannot divide by zero.')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))
