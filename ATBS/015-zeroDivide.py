# This program demonstrates a 'Divide by Zero' error.
# Written in Python 3.5.1

def spam(divideBy):
    return 42 / divideBy

print(spam(2))
print(spam(12))
print(spam(0)) # ERROR! (ZeroDivisionError)
print(spam(1))
