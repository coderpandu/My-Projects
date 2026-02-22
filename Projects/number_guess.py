# ********** Number Guessing Program ********** #

import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)

guesses = 0
is_running = True

print("**** Welcome to the number guessing game from python ****")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:
    num_guess = input(f"Enter a Number: ")
    
    if num_guess.isdigit():
        num_guess = int(num_guess)
        guesses += 1

        if num_guess > highest_num or num_guess < lowest_num:
            print(f"Guess the number between {lowest_num} and {highest_num} !!!")
        
        elif num_guess < answer:
            print("Too low! Try Again!")
        
        elif num_guess > answer:
            print("Too high!! Try Again!")
        
        else:
            print(f"CORRECT ❤️ The answer was {answer}")
            print(f"You took {guesses} guesses")
            is_running = False
                
    else:
        print("Invalid Imput!!")
        print(f"PLEASE Select a number between {lowest_num} and {highest_num}")
             
