from random import randint
import time
# Adding a variable to create an attempt counter
count = 0

#
def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

# Determining the difficulty of the game
def dif_choosing():
    global x
    difficulty = input('Choose a difficulty:\n Easy\n Normal\n Hard\n Or just enter a number greater than one\n')
    if difficulty == 'Easy':
        x = 10
    elif difficulty == 'Normal':
        x = 25
    elif difficulty == 'Hard':
        x = 100
    elif difficulty.isdigit() == True:
        x = int(difficulty)
    elif isfloat(difficulty):
        x = int(round(float(difficulty)))
        print(f'I appreciated your wit, but I figured your number would be {x}')
    else:
        print('I don\'t think I offered you that option, shall we try again?')
        dif_choosing()

# Game itself
def game():
    global count
    gameloop = True
    while gameloop is True:
        global turn
        turn_user = input('Try to guess my number!\n')
        count += 1
        if turn_user.isdigit() == True:
            turn = int(turn_user)
        elif isfloat(turn_user):
            turn = int(round(float(turn_user)))
        else:
            print('Are you sure you entered a number? Let\'s try again')
            continue
        if turn == number:
            gameloop = False
            print(f'I think you guessed it! Congratulations\n The number of times you try: {count}')
        elif turn < number:
            print(f'No, my number is greater than {turn}')
        elif turn > number:
            print(f'No, my number is less than {turn}')

# Implementation of code blocks
dif_choosing()
number = randint(1, x)
print(f'Okay, we\'ve identified the difficulty for you! Now you have to guess a number from 1 to {x}')
game()
