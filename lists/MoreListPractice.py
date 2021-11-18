letters = ["a", "b", "c", "d", "e", "f"]

print("Q1:", letters[1:3])
#prediction: ['b','c',]
#outcome: 

print("Q2:", letters[:4])
#prediction: ['a','b','c','d']
#outcome: 

print("Q3:", letters[3:])
#prediction: ['d','e','f']
#outcome: 

print("Q4:", letters[:])
#prediction: ["a", "b", "c", "d", "e", "f"]
#outcome: 

print("Q5:", letters[:6:2])
#prediction: ["a", "c", "e",]
#outcome: 

print("Q6:", letters[-1:0:-1])
#prediction: ['f','e','d','c','b']
#outcome:

print("Q7:", letters[-1::-1])
#prediction: ['f']
#outcome: ['f','e','d','c','b','a']

letters[1:3] = ["x", "y"]
print("Q8:", letters)
#prediction: ["a", "x", "y", "d", "e", "f"]
#outcome: 

number = letters.index("e")
print("Q9:", number)
#prediction: 4
#outcome: 4

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

winter = months[0:3]
winter.insert(0,months[11])
print(winter)

spring = months[2:6]
print(spring)

summer = months[5:9]
print(summer)

fall = months[8:12]
print(fall)
