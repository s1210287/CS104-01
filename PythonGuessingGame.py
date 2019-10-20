import random

name = input("What is your name?: ")
theComputerNumber = random.randint(1, 1000000)
print(theComputerNumber)
print("Hi " + name + ". I'm thinking of a number between 1 and 1000000.")
numberOfGuesses = 0
lowGuessRange = 1
highGuessRange = 1000000

while numberOfGuesses < 20:
    print("Enter a guess in range from",lowGuessRange, "to", highGuessRange) 
    playerGuess = input("Enter a guess: ")
    playerGuess = int(playerGuess)
    numberOfGuesses = numberOfGuesses + 1 
    if playerGuess < theComputerNumber:
       print("That number is too low")
    elif playerGuess > theComputerNumber:
        print("That number is too high")
    if playerGuess < lowGuessRange:
        print("Guess out of range, try again")
    if playerGuess > highGuessRange:
        print("Guess out of range, try again")
        break
    
    

if guess == number:
    print("You win! Congratulations " + name + " you guessed the correct number!")
else:
    print("Sorry you ran out of tries and lost. The right number was " + number)
    

