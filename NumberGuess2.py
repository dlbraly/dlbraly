"""
Number Gussing game - David Braly
https://github.com/dlbraly

"""

import random


print('This is a number guessing game. ')
wgame = int(input('1. do you want to guess the computers number or 2. do you want the computer to guess your number?'))

if wgame == 1:
    print('How big of a game do you want to play? ')
    x=int(input(f'Your Choice. A number between 1 and What? '))

    def guess(x):
        tries = 1
        random_number = random.randint(1, x)
        guess = 0
        while guess != random_number:
            guess = int(input(f'Guess a number between 1 and {x}: '))
            if guess < random_number:
                print('Sorry, too low. Guess again. ')
                tries += 1
            elif guess > random_number:
                print('Sorry, too high. Guess again. ')
                tries += 1

        print(f'Congrats, you have guessed the number {random_number} correctly in {tries} tries.')
    guess(x)


elif wgame == 2:
    print('How big of a game do you want to play?')
    x=int(input(f'Your Choice. A number between 1 and What?'))

    def computer_guess(x):
        tries = 0
        low = 1
        high = x
        feedback = ''
        while feedback != 'c':
            if low != high:
                guess = random.randint(low, high)
            else:
                guess = low #high or low, they are equal.
            feedback = input(f'Is {guess} too high (H), too low (L), or Correct (C)? ').lower()
            tries += 1
            if feedback == 'h':
                high = guess - 1
            elif feedback == 'l':
                low = guess + 1
        print(f'Yay, the computer has guessed your number {guess} correctly in {tries} tries!')

    computer_guess(x)