# This program demonstrates use of the global statement within a function
# Because 'eggs' is declared global at the top of spam(), when eggs is set to 'spam',
# this assignment is done to the globally scoped 'eggs'.
# No local 'eggs' variable is created.
# Written in Python 3.5.1 on Mac

def spam():
    global eggs
    eggs = 'spam'

eggs = 'global'
spam()
print(eggs)
