# import random library
import random # Error: "random" has a capital when it should not

x = random.randint(1, 100) # Error: "random" is spelled wrong, a comma is missing in the range, and "randint" has a capital I when it should not.

guess = 0
numguesses = 0 # Error: Variables cannot have symbols and declarations do not use operators

# while loop to keep asking for guesses until guess
while guess != x:
    guess = input("Enter a number between 1 and 100: ") # Error: Line was missing a quote and bad spacing between input discription and the input itself
    guess = int(guess) # Error: line was not tabbed correctly

    if guess > 100: # Error: Missing colon and wrong upper limit
        print (guess, "is too big") # Error: Missing parentheses
        numguesses = numguesses + 1 # Error: Wrong variable names
    elif guess < 0: # Error: Line is tabbed wrong and wrong lower limit
        print (guess, "is too small") # Error: Line is tabbed wrong and is missing parentheses
        numguesses = numguesses + 1 # Error: Wrong varible names
    elif guess == x: # Error: There is not win condtion, this should be an elif statement
        print ("Correct!") # Error: "print" should not be capitalized and missing parentheses
        numguesses = numguesses + 1 # Error: Wrong varibale names and tabbing
    # Error: There is no handling for a wrong guess
    else:
        print("Wrong guess, try again.")

print ("You guessed correctly after", numguesses, "guesses") # Error: missing quotes and parentheses and wrong variable name


