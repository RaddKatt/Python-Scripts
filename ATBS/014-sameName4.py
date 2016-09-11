# Another demonstration of local/global variable scoping
# Throws an error due to a local variable that doesn't yet exist
# Written in Python 3.5.1

def spam():
    print(eggs) # ERROR!
    eggs = 'spam local'

eggs = 'global'
spam()
