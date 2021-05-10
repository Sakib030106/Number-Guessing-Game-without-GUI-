# This is a number guessing game.

import random

# Introduction:
name = input("Hi. This is a number guessing game. Please enter your name:")
c = name.title()
print("Welcome,", c)

num = random.randint(1, 1000)    # range of numbers
attempts = 0     # times tried

# Engine:
while True:
    try:
        # Taking User Input:
        input_num = input("Guess a number between(1 to 1000): ")
        input_num = int(input_num)
        attempts += 1

        if input_num == num:
            print("Congratulations! You guessed currect. ")
            break
        elif input_num > num:
            print("Incorrect. Please enter a smaller number. ")
        else:
            print("Incorrect. Please enter a larger number. ")
    except ValueError:
        print("Invalid input. Try again! ")
        continue
print("You tried", attempts, "times to find the numbers. ")

# End:
end = input("Thank you for using this program. See you again! ")
