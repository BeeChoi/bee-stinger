import random 

print("Let's play rock paper scissors!!")

gameState = input("Ready to play? (y or n) ")
numWins = 0 
gamesPlayed = 0

while gameState == "y":
	# 1=rock 2=paper 3=scissors
  computerChoice = random.randint(1,3)
  userChoice = int(input("Enter 1 for Rock, 2 for Paper, or 3 for Scissors "))
  if userChoice == 1:
    print("You chose rock!")
    #user chose rock
    # 1=rock 2=paper 3=scissors
    if computerChoice == 1:
      print("The computer chose rock!")
      print("Tie Game!")
      gamesPlayed += 1
    elif computerChoice == 2:
      print("The computer chose paper!")
      print("Paper covers rock!\nYou lost")
      gamesPlayed += 1
      gameState = "n"
      gameState = input("Do you want to play again? (y or n) ")
    elif computerChoice == 3:
      print("The computer chose scissors!")
      print("Rock squishes scissors\nYou win!!")
      gamesPlayed += 1
      numWins += 1
  elif userChoice == 2:
    print("You chose paper!")
    #user chose paper
    # 1=rock 2=paper 3=scissors
    if computerChoice == 1:
      print("The computer chose rock!")
      print("Paper covers rock!\nYou win!")
      gamesPlayed += 1
      numWins += 1
    elif computerChoice == 2:
      print("The computer chose paper!")
      print("Tie Game!")
      gamesPlayed += 1
    elif computerChoice == 3:
      print("The computer chose scissors!")
      print("Scissors cut paper\nYou lost")
      gamesPlayed += 1
      gameState = "n"
      gameState = input("Do you want to play again? (y or n) ")
  elif userChoice == 3:
    print ("You chose scissors")
      #user chose scissors
      # 1=rock 2=paper 3=scissors
    if computerChoice == 1:
      print("The computer chose rock!")
      print("Rock squishes scissors\nYou lost")
      gamesPlayed += 1
      gameState = "n"
      gameState = input("Do you want to play again? (y or n) ")
    elif computerChoice == 2:
      print("The computer chose paper!")
      print("Scissors cut paper\nYou win!!")
      gamesPlayed += 1
      numWins = 1
    elif computerChoice == 3:
      print("The computer chose scissors!")
      print("Tie Game!")
      gamesPlayed += 1
  else: 
    print("Bad input!! You lose")
    gamesPlayed += 1
    gameState = "n"
    gameState = input("Do you want to play again? (y or n) ")

print("Thanks for playing")
print("You won", numWins, "games out of", gamesPlayed)

'''
1. Explain here what the code is doing
2. How the code is structured
3. How you fixed the errors
'''

'''
1. The code is a rock, papers, scissors game. The user inputs a number and then the computer picks a random number from 1 to 3. It then uses a series of if, elif, and else conditions to see who the winner is depending on the choice of the user and computer. The code also keeps track of the wins and looses to print at the end of the gamesPlayed

2. The code declared the import statement first and the proceeds to tell the use the fucntion of the code. Most of the variables are declared towards the top of the code. Underneath are a while loop. In the Loop are ifs, elifs, and elses that check for the following: User choice, bad input, computer choice, and win/loose conditions. Outside of the loop are print statements that print when the loop ends (when the user looses or a bad input is detected). They thank the user for playing and tell the number of wins vs games played.

3. I fixed the errors by chaging spelling mistakes in varibales. I also fixed capitalization and spacing of variables. In addition, I added and removed parentheses and quotations where needed. I fixed inncorect variables in some locations and I fixed if statements that should've been elifs. There were also tabbing erros that needed to be corrected. I also fixed the import statement and added lines to add to the gamesplayed and winned where needed.'''
