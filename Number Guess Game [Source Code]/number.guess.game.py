# This is a number guessing game.

# Introduction:
name = input('Hi! Welcome to this game. Please enter your name: ')
c = name.title()
print('Welcome,', c)

import random     # Importing turtle module:

num = random.randint(1, 1000)
attempts = 0

# Engine:
while True:
    try:
        input_num = input('Guess the number (between 1 to 1000): ')
        input_num = int(input_num)
        attempts += 1

        if input_num == num:
            print('Yes, your guess is correct! ')
            break
        if input_num > num:
            print('Incorrect! Please try to guess a smaller number. ')
        else:
            print('Incorrect! Please try to guess a larger number. ')
    except ValueError:
        print('Invalid Input. Try again. ')
        continue
print('You tried', attempts, 'times to find the number. ')

# End:
end = input('Thank you for playing this game! See you soon.')