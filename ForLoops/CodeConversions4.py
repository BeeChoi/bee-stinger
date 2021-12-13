#Part 1: Convert this for loop to a while loop
print("\nPart 1")
dogs = ["Lab", "Poodle", "Bulldog", "Beagle", "Terrier", "Corgi", "Yorkie"]
for number in range(0, 7): # repeats the loop while the number is between 0 and 7
	print(dogs[number]) # prints the item at the index equal to the number range

# 1) How what values does *number* equal as this for loop runs?
# 0, 1, 2, 3, 4, 5, 6
# 2) What do these numbers represent in terms of the list, *dogs*?
# "Lab", "Poodle", "Bulldog", "Beagle", "Terrier", "Corgi", "Yorkie

#Part 1: Write *while* loop here
counter = 0
dogs = ["Lab", "Poodle", "Bulldog", "Beagle", "Terrier", "Corgi", "Yorkie"]
while counter < 7:
  print(dogs[counter])
  counter += 1




#Part 1: Write a for loop here that loops through the elements of *dogs*
dogs = ["Lab", "Poodle", "Bulldog", "Beagle", "Terrier", "Corgi", "Yorkie"]
for dog in dogs:
  print(dog)


#Part 2:
print("\nPart 2")
#Remember dogs[number] indexes the list dogs at a specific index!

#Now recall slicing:
dogs = ["Lab", "Poodle", "Bulldog", "Beagle", "Terrier", "Corgi", "Yorkie"]

print(dogs[0:4]) # prints lab to but not including terrier
print(dogs[:4]) # print lab to but not including terrier

print(dogs[4:7]) # prints terrier - yorkie
print(dogs[4:]) # prints terrier - yorkie

print(dogs[0:7:2]) # prints lab, bulldog, terrier, yorkie

start = 2
end = 5
print(dogs[start:end]) #


dogs[0:2] = ["Labrador", "Golden Doodle"] # sets the lab and poodle to labrador to golden doodle
print(dogs) 

#Write code to print ["Poodle", "Beagle", "Corgi"] using slicing
dogs = ["Lab", "Poodle", "Bulldog", "Beagle", "Terrier", "Corgi", "Yorkie"]
print(dogs[1:7:2])


#Part 3:
print("\nPart 3")

name = "Barbra"
print("Hello " + name + "!")
# 3) What does the previous line print out and why?
# Hello Barbra!. The plus prints without a space.

fullName = name + " Streisand"
print(fullName) 
# 4) What does the previous line print out and why?
# Barbra Streisand, you're adding a string to  string

fruit = "melon"
fruits = fruit + "s"
print(fruits)
# 5) What does the previous line print out and why?
# melons, the plus does not add a space when you appened S to the string



######## GO BACK TO CODE CONVERSIONS PART 1 AND CHECK FOR MISTAKES AND RESUBMIT WITH FIXES ##########
