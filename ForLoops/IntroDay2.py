#from time import sleep
for x in range(11):
  print(x**2)

print("\n---------------------\n")

floor0 = ['empty', 'sword', 'monster', 'magic stone', 'stairs up']
currentRoom = 0

for room in floor0:
  if room == "monster":
    floor0[currentRoom] = "empty"
  print(floor0[currentRoom])
  print(floor0)
  currentRoom += 1

print("\n---------------------\n")

sum = 0
for x in range(0,11,2):
  sum = sum + x
  print(sum)

print("\n---------------------\n")

numLoop = int(input("How many times do you want to repeat this loop? "))
#numLoop += 1

for i in range(numLoop):
  loopInput = input("Put something here: ")
  print(loopInput, "is/are very cool.")
