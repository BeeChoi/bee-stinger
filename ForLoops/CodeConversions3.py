#######Part 1:
# Write in what prints out for the following print statements on the comment next to print statement 
print("Part 1")
numbers = [4, 6, 2, 15, 9, 3] 
print(numbers[0]) # Prints 4
print(numbers[1]) # Prints 6
print(numbers[2]) # Prints 2
print(numbers[3]) # Prints 15
print(numbers[4]) # Prints 9
print(numbers[5]) # Prints 3

counter = 4
print(numbers[counter]) # Prints 9



#######Part 2:
print("Part 2")

counter = 0
numbers = [4, 6, 2, 15, 9, 3] 
# 1) How many items are in this list?
# 6 Items
# 2) What are the indexes of the elements in the list
# 0, 1, 2, 3, 4, 5
# 3) What values does counter equal as it loops?
# 0, 1, 2 3, 4, 5
while counter < 6:
	print(numbers[counter]) #
	counter = counter + 1



# 4) Why does this while loop need to loop 6 times?
# Because there are 6 items in the list with indicies 0-5

#Part 2: Write for loop here for the above while loop

numbers = [4, 6, 2, 15, 9, 3] 
for i in range(6):
  print(numbers[i])



#######Part 3:
print("\nPart 3")

counter = 0
numbers = [4, 6, 2, 15, 9, 3] 
# 5) How many items are in this list?
# 6
# 6) What does len(numbers) do?
# gets the length of this list, in this case 6
while counter < len(numbers): 
	print(numbers[counter]) #prints the number at the index with value equal to counter
	counter = counter + 1


#Part 3: Write for loop here for the above while loop

numbers = [4, 6, 2, 15, 9, 3] 
for i in range(len(numbers)):
  print(numbers[i])


#Part 4: Now I am going to make the list longer!
print("\nPart 4")

counter = 0
numbers = [4, 6, 2, 15, 9, 3, 20, 5, 10, 7, 13] 
# 5) How many items are in this list?
# 11
# 6) I copied and pasted the code from question 2. Will the same code work using this new list? Why or why not? 
# Yes, it will since the variable names remain constant, however, it will not cycle through the whole list
while counter < len(numbers): 
	print(numbers[counter]) #
	counter = counter + 1
