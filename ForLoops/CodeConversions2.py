#Part 1:
print("Part 1")
counter = 0
numbers = []
# 1) What values does counter equal as it loops?
# 0, 1, 2, 3, 4, 5, 6
while counter < 7: 
	num = int(input("Enter a number: "))
	numbers.append(num) # Appends the inputted number to the "numebers" list
	counter = counter + 1 # Increases the counter value by one

print("Final list is:", numbers) #

# 2) What does the counter variable do in this while loop?
# It causes the loop to cycle through until the counter reaches 7

#Part 1: Write for loop here for the above while loop

numbers = []
for i in range(7):
  num = int(input("Enter a number: "))
  numbers.append(num)
print("Final list is:", numbers)

#Part 2:
print("\nPart 2")
counter = 0
numbers = []
# 3) What values does counter equal as it loops?
# 0, 2, 4, 6, 8
while counter < 10:
	num = int(input("Enter a number: "))
	numbers.append(num) # Appends the inputted number to the "numebers" list

	counter = counter + 2 # Increases the counter by 2 each time it loops

print("Final list is:", numbers) # Prints "Final list is: " and the final list of numbers, formatted as a list

#Part 2: Write for loop here for the above while loop

numbers = []
for i in range(0,10,2):
  num = int(input("Enter a number: "))
  numbers.append(num)
print("Final list is:", numbers)

# 4) What variable is required in the while loop but is not needed in the for loop you wrote above?
# counter

#Part 3:
print("\nPart 3")
counter = 4
numbers = []
# 5) What values does counter equal as it loops?
#4, 3, 2, 1

while counter > 0:
	num = int(input("Enter a number: "))
	numbers.append(num) # Appends the inputted number to the "numebers" list

	counter = counter - 1 # Decreases the counter by 1 each time it loops

print("Final list is:", numbers) # Prints "Final list is: " and the final list of numbers, formatted as a list

#Part 3: Write for loop here for the above while loop

numbers = []
for i in range(4, 0, -1):
  num = int(input("Enter a number: "))
  numbers.append(num)
print("Final list is:", numbers)

# 6) What variable did you not need and why?
#counter since the for loop cycles through the range on its own
# 7) Do the values inputted by the user change the way the code is functioning?
# No, however it will change the output based on the numbers imputted.
