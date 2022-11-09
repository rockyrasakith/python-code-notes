# Guessing a number game. Simple program
import random

name = input("What is your name? ")
print(f"Hello {name}. Let's play a game! Guess random number between 1 and 20.")

secretNumber = random.randint(1, 20)
print(f"DEBUG: Secret number is {secretNumber}")

for guessesTaken in range(1, 7):
    print("Take a guess.")
    guess = int(input())

    if guess < secretNumber:
        print("Your guess is too low.")
    elif guess > secretNumber:
        print("Your guess is too high.")
    else:
        break #this condition is for the correct guess

if guess == secretNumber:
    print(f"Good job {name}. You guessed my number in {guessesTaken} guesses.")
else:
    print(f"Nope, the number I was thinking was {secretNumber}")
