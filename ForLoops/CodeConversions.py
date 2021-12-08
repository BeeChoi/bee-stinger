#Question 1: Convert this while loop to a for loop
print("Question 1")
counter = 0
total = 0
while counter < 5: #loop condition stop the loop when counter = 5
	number = input("Enter a number: ")
	number = int(number) # string -> integer

	total = total + number #totaling user input
	
	counter = counter + 1

print("Final total is:", total) #outside 

#Question 1: Write for loop here

total = 0
for counter in range(5):
  number = int(input("Enter a number: "))
  total = total + number
print("Final total is:", total) 

#Question 2: Convert this while loop to a for loop
print("\nQuestion 2")
import random
counter = 1
numbers = [] # defines a new list
while counter < 11: # continues the loop until the counter value reaches 11
	rando = random.randint(counter, 10) # generates a random integer between the counter value and 10 and sets it equal to rando
	numbers.append(rando) # adds the random number to the numbers list
	counter = counter + 1

print(numbers)

#Question 2: Write for loop here

from random import randint
numbers = []
for i in range(10):
  rando = randint(i, 10)
  numbers.append(rando)
print(numbers)

#Question 3: Convert this while loop to a for loop
print("\nQuestion 3")
total = 0
counter = 0
numbers = [4, 6, 2, 15, 9, 3] #what is the total of these numbers? 39
while counter < len(numbers): # Repeats the loop while the counter is less than the amount of items in the list
	total = total + numbers[counter] # adds the total with the number with the index of the counter
	counter = counter + 1
print(total) #does it match what you expected? Yes

#Question 3: Write for loop here
total = 0
numbers = [4, 6, 2, 15, 9, 3]
for i in range(len(numbers)):
  total = total + numbers[i]
print(total)

#Question 4: Convert this for loop to a while loop
print("\nQuestion 4")
strings = ["bob", "winter", "cat", "kitchen", "goose"]
for number in range(5): # creates temporary variable number and repeats while number is between 0 and 5
	print(strings[number]) # prints the item in the list with the index of the number variable

#Question 4: Write while loop here

counter = 0
strings = ["bob", "winter", "cat", "kitchen", "goose"]
while counter < 5:
  print(strings[counter])
  counter += 1

#Question 4: Write an equivalent for loop here

strings = ["bob", "winter", "cat", "kitchen", "goose"]
for i in strings:
  print(i)
