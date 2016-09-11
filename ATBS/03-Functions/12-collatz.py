# The Collatz Sequence
# 'The simplest impossible math problem'
# Provide any number, and using this sequence you will always arrive at 1!
# Written in Python 3.5.1 on Mac

def isEven(number):
    if number % 2 == 0:
        return True
    else:
        return False

def collatz(number):
    if isEven(number):
        result = number // 2
        return result
    else:
        result = 3 * number + 1
        return result

def getAnswer(valueGiven):
    if isEven(collatz(valueGiven)):
        return '\033[1m' + str(collatz(valueGiven)) + '\033[0m' + '\t(result: even)'
    else:
        return '\033[1m' + str(collatz(valueGiven)) + '\033[0m' + '\t(result: odd)'

def printResults(number):
    if isEven(valueGiven):
        answer = getAnswer(valueGiven)
        print(' (even)\t' + '\033[1m' + str(valueGiven) + '\033[0m' + ' // 2 = ' + answer)
    else:
        answer = getAnswer(valueGiven)
        print(' (odd)\t3 * ' + '\033[1m' + str(valueGiven) + '\033[0m' + ' + 1 = ' + answer)

print('\r')
while True:
    try:
        valueGiven = int(float(input('Type an integer: ')))
        print('\r')
        printResults(valueGiven)

        while collatz(valueGiven) != 1:
            valueGiven = collatz(valueGiven)
            printResults(valueGiven)
        print('\r')
        break
    except ValueError:
        print('-- Must type a whole number. Try again.\n')
        continue
