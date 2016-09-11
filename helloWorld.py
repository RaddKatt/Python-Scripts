# Basic Hello World program
# This program says 'hello' and asks for the user's name
# Written on Python 3.5.1

print('Hello, world!')
myName = input('What is your name? ') # asks for their name
print('It is good to meet you, ' + myName + '.')
print('The length of your name is: ' + str(len(myName)) + ' characters.')
myAge = input('What is your age? ')# asks for their age
print('You will be ' + str(int(myAge) + 1) + ' in a year.')
