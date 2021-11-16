from time import sleep
play = "yes"
points = 0
guessNum = 0
WrongGuesses = []

while play == "yes":
    sleep(0.5)
    print("Hello, and welcome to my very cool trivia game.")
    sleep(0.5)
    print("Please enter your answers in lower case letters only.")
    sleep(0.5)
    
    Answer1 = input("What is Avogadro's number? (Express as: Yx10^YY) ")
    
    while Answer1 != "6.02x10^23":
        if Answer1 in WrongGuesses:
          print("You've already guessed this")
          Answer1 = input("What is Avogadro's number? (Express as: Yx10^YY) ")
        else:
          print("Wrong Answer")
          WrongGuesses.append(Answer1)
          guessNum += 1
          points -= 1
          Answer1 = input("What is Avogadro's number? (Express as: Yx10^YY) ")
    
    print("Right Answer!")
    
    if guessNum > 0:
        #points -= 1
        guessNum = 0
    else:
        points += 3
        guessNum = 0
    
    WrongGuesses.clear()
    
    sleep(0.5)
    
    Answer2 = input("Who was the 40th President of the United States? ") 
    
    while Answer2 != "ronald reagan":
        if Answer2 in WrongGuesses:
          print("You've already guessed this")
          Answer2 = input("Who was the 40th President of the United States? ") 
        else:
          print("Wrong Answer")
          WrongGuesses.append(Answer2)
          guessNum += 1
          points -= 1
          Answer2 = input("Who was the 40th President of the United States? ") 
    
    print("Right Answer!")
    
    if guessNum > 0:
        #points -= 1
        guessNum = 0
    else:
        points += 3
        guessNum = 0
    
    WrongGuesses.clear()
    
    sleep(0.5)
    
    Answer3 = input("Who is the main character in the movie Catch Me If You Can? ") 
    
    while Answer3 != "frank abagnale":
        if Answer3 in WrongGuesses:
          print("You've already guessed this")
          Answer3 = input("Who is the main character in the movie Catch Me If You Can? ")
        else:
          print("Wrong Answer")
          WrongGuesses.append(Answer3)
          guessNum += 1
          points -= 1
          Answer3 = input("Who is the main character in the movie Catch Me If You Can? ") 
    
    print("Right Answer!")
    
    if guessNum > 0:
        #points -= 1
        guessNum = 0
    else:
        points += 3
        guessNum = 0
    
    WrongGuesses.clear()
    
    sleep(0.5)
    
    Answer4 = input("What lines have a blue color in the New York City Subway? (separate ONLY with a comma. Ex: 1,2,3) ") 
    
    while Answer4 != "a,c,e":
        if Answer4 in WrongGuesses:
          print("You've already guessed this")
          Answer4 = input("What lines have a blue color in the New York City Subway? (separate ONLY with a comma. Ex: 1,2,3) ")
        else:
          print("Wrong Answer")
          WrongGuesses.append(Answer4)
          guessNum += 1
          points -= 1
          Answer4 = input("What lines have a blue color in the New York City Subway? (separate ONLY with a comma. Ex: 1,2,3) ")
    
    print("Right Answer!")
    
    if guessNum > 0:
        #points -= 1
        guessNum = 0
    else:
        points += 3
        guessNum = 0
    
    WrongGuesses.clear()
    
    sleep(0.5)
    
    Answer5 = input("What year was the first version of Windows released? ") 
    
    while Answer5 != "1985":
        if Answer5 in WrongGuesses:
          print("You've already guessed this")
          Answer5 = input("What year was the first version of Windows released? ")
        else:
          print("Wrong Answer")
          WrongGuesses.append(Answer5)
          guessNum += 1
          points -= 1
          Answer5 = input("What year was the first version of Windows released? ")
    
    print("Right Answer!")
    
    WrongGuesses.clear()
    
    if guessNum > 0:
        #points -= 1
        guessNum = 0
        play = "no"
    else:
        points += 3
        guessNum = 0
        play = "no"

if points <= 6:
    sleep(0.5)  
    print("You Lost!")
    sleep(0.5)
    print("You earned", points, "points.")
    sleep(0.5)
    print("Thank you for playing!")
elif points > 6:
    sleep(0.5)
    print("You Won!")
    sleep(0.5)
    print("You earned", points, "points.")
    sleep(0.5)
    print("Thank you for playing!")
