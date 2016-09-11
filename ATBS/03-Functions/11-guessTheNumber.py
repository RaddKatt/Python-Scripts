# Written in Python 3.5.1
# This is a guess the number game.

import random

secretNumber = random.randint(1,20)
print('I am thinking of a number between 1 and 20.')

# Ask the player to guess 6 times:
for guessesTaken in range(1,7):
    if guessesTaken == 6:
        print('Nope. The number I was thinking of was ' + str(secretNumber) + '.')
        break
    else:
        try:
            guess = int(input('Trial #' + str(guessesTaken) + ' - Take a guess: '))
            if guess > 20:
                print('-- Value must be between 1 and 20.')
            elif guess < secretNumber:
                print('-- Your guess is too low.')
            elif guess > secretNumber:
                print('-- Your guess is too high.')
            else:
                print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
                break
        except ValueError:
            print('Error. Value must be a number.')
