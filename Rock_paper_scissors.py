# Rock paper scissors
# Nmerous improvements were made- the number of lines used was decreased and the process by which the program chose "rock", "paper", or "scissors" was simplified.


import random

play_or_not = 'start'

while play_or_not == 'start':

    your_choice = input('Enter your choice of "rock", "paper", or "scissors" ')

    program_choice = random.choice(['rock', 'paper', 'scissors'])

        
    if (your_choice == 'rock' and program_choice == 'scissors') or (your_choice == 'paper' and program_choice == 'rock') or (your_choice == 'scissors' and program_choice == 'paper'):
        
        print(f'Python chose {program_choice}.')
        print('You win!')
        play_or_not = input('To play the game, type "start". To stop, type anything else. ')
        
    elif (your_choice == 'rock' and program_choice == 'paper') or (your_choice == 'paper' and program_choice == 'scissors') or (your_choice == 'scissors' and program_choice == 'rock'):
        
        print(f'Python chose {program_choice}.')
        print('You lose!')
        play_or_not = input('To play the game, type "start". To stop, type anything else. ')

    elif your_choice == program_choice:
        print(f'Python chose {program_choice}.')
        print("It's a draw!")
        play_or_not = input('To play the game, type "start". To stop, type anything else. ')

    else:
        print('Error. Please enter a valid choice.')
        play_or_not = input('To play the game, type "start". To stop, type anything else. ')

