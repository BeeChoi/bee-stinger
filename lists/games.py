# Starter Code

videoGames = ["Mario", "Sonic", "Joust", "Zelda"]

videoGames.append("Minecraft")

Choice = int(input("Pick a number to choose a game (0-4): "))
print(videoGames[Choice])

Cont = "Y"

while Cont == "Y":
  Game = input("Name a game: ")
  isIn = videoGames.count(Game)
  if isIn > 0:
    videoGames.remove(Game)
    print(videoGames)
  if isIn == 0:
    videoGames.append(Game)
    print(videoGames)
  Cont = input("Do you want to continue? [Y/N] ")

insItem = input("What item do you want to insert? ")
insIndex = int(input("At what index do you want to insert the item? "))
videoGames.insert(insIndex, insItem)
print(videoGames)
