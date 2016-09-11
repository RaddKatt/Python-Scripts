# This program demonstrates local and global variables with the same name
# This is for POC. Initializing local and global variables with the same name is not recommended.
# Written in Python 3.5.1

def spam():
    eggs = 'spam local'
    print(eggs) # prints 'spam local'

def bacon():
    eggs = 'bacon local'
    print(eggs) # prints 'bacon local'
    spam()
    print(eggs) # prints 'bacon local'

eggs = 'global'
bacon()
print(eggs) # prints 'global'
