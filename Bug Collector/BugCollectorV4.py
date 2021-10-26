start = input("Do you want to play? [Y/N] ")
numBugs = 0
totalBugs = 0
while start == "Y":
    numBugs = int(input("How many bugs did you catch today? "))
    if numBugs < 0:
        print("Error | No Negative Numbers.")
        #exit()
    else:
        totalBugs = totalBugs + numBugs
    start = input("Do you want to continue? [Y/N] ")
print(totalBugs, "bugs caught.")