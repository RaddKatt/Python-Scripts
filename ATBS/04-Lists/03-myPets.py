# This program demonstrates checking a value in a list using the 'not in' operator
# Written in Python 3.5.1 on Mac

myPets = ['Zophie', 'Pooka', 'Fat-tail']

while True:
    name = input('Enter a pet name: ')
    if name not in myPets:
        print('I do not have a pet named ' + name + '.')
        print('Try again.')
    else:
        print(name + ' is my pet!')
        break
