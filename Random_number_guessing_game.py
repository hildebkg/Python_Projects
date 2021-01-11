# Random number guessing game

import random

print('Welcome to the guess the random number game! Please choose a range of numbers \
over which you want the program to generate a random number. Then, enter your guess.')

a = int(input('Enter the first number in the desired range: '))
b = int(input('Enter the last number in the desired range: '))
guess = int(input('Enter your guess: '))

rand_num = random.randint(a,b)

while guess != rand_num:
    if guess > rand_num:
        print('Your guess is too high. Try again.')
        guess = int(input('Enter your guess: '))
    elif guess < rand_num:
        print('Your guess is too low. Try again.')
        guess = int(input('Enter your guess: '))

print('Correct! The random number was {0}.\n'.format(rand_num))

