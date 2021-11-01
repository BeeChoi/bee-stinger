
play = "yes"
points = 0
guessNum = 0
while play == "yes":

    print("Hello, and welcome to my very cool trivia game.")

    print("Please enter your answers in lower case letters only.")

    Answer1 = input("Question 1 ")
    while Answer1 != "Answer 1":
        print("Wrong Answer")
        guessNum += 1
        Answer1 = input("Question 1 ")
    print("Right Answer!")
    if guessNum > 0:
        points -= 1
        guessNum = 0
    else:
        points += 3
        guessNum = 0

    Answer2 = input(" ") 
    while Answer2 != " ":
        print("Wrong Answer")
        guessNum += 1
        Answer2 = input(" ")
    print("Right Answer!")
    if guessNum > 0:
        points -= 1
        guessNum = 0
    else:
        points += 3
        guessNum = 0

    Answer3 = input("  ") 
    while Answer3 != "f ":
        print("Wrong Answer")
        guessNum += 1
        Answer3 = input("  ")
    print("Right Answer!")
    if guessNum > 0:
        points -= 1
        guessNum = 0
    else:
        points += 3
        guessNum = 0

    Answer4 = input(" ") 
    while Answer4 != " ":
        print("Wrong Answer")
        guessNum += 1
        Answer4 = input("")
    print("Right Answer!")
    if guessNum > 0:
        points -= 1
        guessNum = 0
    else:
        points += 3
        guessNum = 0

    Answer5 = input(" ") 
    while Answer5 != " ":
        print("Wrong Answer")
        guessNum += 1
        Answer5 = input(" ")
    print("Right Answer!")
    if guessNum > 0:
        points -= 1
        guessNum = 0
        play = "no"
    else:
        points += 3
        guessNum = 0
        play = "no"
if points <= 6:
 
    print("You Lost!")

    print("You earned", points, "points.")

    print("Thank you for playing!")
elif points > 6:

    print("You Won!")

    print("You earned", points, "points.")

    print("Thank you for playing!")
