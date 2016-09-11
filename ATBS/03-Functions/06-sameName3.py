# Another demonstration of local/global variable scoping
# Written in Python 3.5.1 on Mac

def spam():
    global eggs
    eggs = 'spam' # this is the global variable

def bacon():
    eggs = 'bacon' # this is a local variable

def ham():
    print(eggs) # this is the global variable

eggs = 42 # this is the global variable

spam()
print(eggs)
