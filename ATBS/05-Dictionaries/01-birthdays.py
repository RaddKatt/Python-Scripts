"""
This program demonstrates using dictionaries to store a group of key/value pairs.
Unlike Lists, which are ordered, dictionaries are unordered.
Written in Python 3.5.1 on Mac
"""

birthdays = {'Alice':'Apr 1',
    'Bob':'Dec 12',
    'Carol':'Mar 4'}

while True:
    name = str(input('Enter a name (blank to quit): '))
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name + '.')

    else:
        print('I do not have birthday information for ' + name)
        bday = str(input('What is their birthday? '))
        birthdays[name] = bday
        print('Birthday database updated.')
