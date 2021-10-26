dayNum = 1
totalBugs = 0
while dayNum in range (1,6):
    numBugs = int(input("How many bugs did you catch today? "))
    if numBugs >= 0:
        totalBugs = totalBugs+numBugs
        print(totalBugs, "bugs caught.")
        dayNum += 1
    else:
        print("Bad input.")
        exit()