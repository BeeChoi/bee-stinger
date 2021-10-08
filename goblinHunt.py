from random import randint
from time import sleep

answer = randint(1,5)
numCupboard = 5
print("Welcome to the Agnry Goblin Hunt, a very epic game of adventure and excitement.")
name = input("What is your name? ")

print("Hello", name + ", do you think you can find the goblin hiding in the kitchen cupboards? ")
sleep(1)
print("Yes?")
sleep(2)
print("Great!")
sleep(1.5)
print("|_| |_| |_| |_| |_|")
sleep (1)

guess = int(input("Which cupboard do you think the goblin is in? "))

if guess > numCupboard or guess < 0:
    print("Bad Input.")
elif guess == answer:
    print("Very neat, you fouund the goblin!")
else:
    print("Wrong Guess. Try again.")