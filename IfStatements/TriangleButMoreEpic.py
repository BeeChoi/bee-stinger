SideOne = int(input("What is the measurement of your first side? "))
SideTwo = int(input("What is the measurement of your second side? "))
SideThree = int(input("What is the measurement of your third side? "))
Continue = "Y"
Perimeter = SideOne + SideTwo + SideThree

while Continue == "Y":
    if (SideOne+SideTwo <= SideThree) or (SideOne+SideThree <= SideTwo) or (SideTwo+SideThree <= SideTwo):
        print("Not a triangle")
        Continue = input("Do you want to continue? [Y/N] ")
        
    elif (SideOne == SideTwo) and (SideTwo == SideThree):
        print("Equilateral Triangle")
        print("The perimeter of your triangle is", Perimeter, "units.")
        Continue = input("Do you want to continue? [Y/N] ")

    elif ((SideOne == SideTwo) and (SideTwo != SideThree)) or ((SideThree == SideTwo) and (SideTwo != SideOne)) or ((SideThree == SideOne) and (SideOne != SideTwo)):
        print("Isosceles Triangle")
        print("The perimeter of your triangle is", Perimeter, "units.")
        Continue = input("Do you want to continue? [Y/N] ")

    elif (SideOne != SideTwo and SideTwo != SideThree and SideThree !=  SideOne):
        print("Scalene Triangle")
        print("The perimeter of your triangle is", Perimeter, "units.")
        Continue = input("Do you want to continue? [Y/N] ")
print("Goodbye!")