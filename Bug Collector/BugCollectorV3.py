numBugs = 0
totalBugs = 0
while numBugs >=0:
    totalBugs = totalBugs + numBugs
    numBugs = int(input("How many bugs did you catch today? "))
print(totalBugs, "bugs caught.")