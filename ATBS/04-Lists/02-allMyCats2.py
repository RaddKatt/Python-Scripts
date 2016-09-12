# This program demonstrates using a single list
# to store any number of items that the user types in.
# Written in Python 3.5.1 on Mac

catNames = [] # Created an empty lists
print('\r')
while True:
    name = input('Enter the name of cat ' + str(len(catNames) + 1) + ' (Or enter nothing to stop.): ')
    if name == '':
        break
    catNames += [name] # list concatenation

print('\nThe cat names are:')
for name in catNames:
    print('-- ' + name)
print('\r')
