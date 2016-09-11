# This program demonstrates defining and using functions
# Written in Python 3.5.1 on Mac

def hello():
    print('\tHowdy!')
    print('\tHowdy!!!')
    print('\tHello there.\n')

print('\r')
for i in range(1,4,1):
    print('Saying hellos #' + str(i) + ':')
    hello()
