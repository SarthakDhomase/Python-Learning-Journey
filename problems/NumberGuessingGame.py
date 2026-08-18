# Problem: Create a number guessing game
# Approach: use the random moudel and 

import random

low = 1
high = 100

answer = random.randint(low , high) # we generate a random number with in our range for the players to guess and store it in variabel anwer 
gueses = 0 # store the number of guess it took to get the answer

is_running = True

print("Python Number Guessing Game")
print(f"Select a number between {low} and {high}")

while is_running:
    guess = input("Enter your guess:  ")
    if guess.isdigit():
        guess = int(guess)
        gueses += 1


        if guess < low or guess > high:
            print("Entered number is out of range ")
            print(f"Please Select a number between {low} and {high}")
        elif guess < answer:
            print("Entered number is lower, try guessing higher")
        elif guess > answer:
            print("Entered number is higher, try guessing lower")
        else:
            print(f"CORRECT! The anser was {answer}")
            print(f"Number of guesses:  {gueses}")
            is_running = False
    else:
        print("Invalid guess")
        print(f"Please Select a number between {low} and {high}")
