
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'] # Define a list of vowels
phrase = str(input("Enter a word/phrase: ")) # Asks for an input to remove vowels from the user
newword = "" # Adds a new string to which we can append the characters to

for letter in phrase: # For loop to cycle through the list
  if letter in vowels: # Checks to see if the letter in the string is a vowel
    print("A vowel has been removed\n") # Prints this if there is a vowel instead of inserting the character into the list
  else:
    newword = newword + letter # Appends the character to the new word
print(newword) # prints the new word
