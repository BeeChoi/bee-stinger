import random

#Coin Flip
rand = random.randint(1,2)
print("Your coin number is",rand)

#6 Sided Dice
rand2 = random.randint(1,6)
print("Your dice number is",rand2)

#Inputted Side Number
rand3 = int(input("How many sides can this dice have? "))
print("This dice has",random.randint(1,rand3),"sides")

#2 Randoms, Multiply to 20
rand4 = random.randint(1,20)
rand5 = random.randint(1,10)
print("Numbers multiplied are",rand4*rand5)