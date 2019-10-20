import random

name = input("What is your name?: ")
number = random.randint(1, 1000000)
print("Hi " + name + ". I'm thinking of a number between 1 and 1000000.")
guesses = 0
lowGuessRange = 1
highGuessRange = 1000000
while guesses < 20:
    guess = input("Enter a guess: ")
    guess = int(guess)
    guesses = guesses + 1
    if guess < number:
        print("That number is too low")
    elif guess > number:
        print("That number is too high")
    if guess < lowGuessRange or guess > highGuessRange:
        print("Guess out of range, try again")
    if guess == number:
        break

if guess == number:
    guesses = str(guesses)
    print("You win! Congratulations " + name + " you gussed the correct number!")

if guess == number:
    number = str(number)
    print("Sorry you ran out of tries and lost. The right number was " + number)
        
