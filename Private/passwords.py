import random

AlphaLower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] # 26
AlphaUpper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] # 26
Numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'] # 10
UnshiftSymbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '[', ']', ';', ',', '.', '/'] # 18
ShiftSymbols = ['_', '+', '{', '}', '|', ':', '"', '<', '>', '>', '?'] # 11

NewPassword = ""
cont = "Y"

while cont == "Y":
    length = int(input("How long do you want your password to be? "))
    complexity = int(input("How complex would you like your password to be? Enter an integer value between 1-3: "))
    if complexity == 1:
        NewPassword = ""
        for i in range(length):
            ListIndex = random.randint(0, 25)
            char = AlphaLower[ListIndex]
            NewPassword = NewPassword + char
        print(NewPassword)
    elif complexity == 2:
        NewPassword = ""
        for i in range(length):
            ListSelect = random.randint(1, 3)
            if ListSelect == 1:
                ListIndex = random.randint(0, 25)
                char = AlphaLower[ListIndex]
                NewPassword = NewPassword + char
            if ListSelect == 2:
                ListIndex = random.randint(0, 25)
                char = AlphaUpper[ListIndex]
                NewPassword = NewPassword + char 
            if ListSelect == 3:
                ListIndex = random.randint(0, 9)
                char = Numbers[ListIndex]
                NewPassword = NewPassword + char
        print(NewPassword)
    elif complexity == 3:
        NewPassword = ""
        for i in range(length):
            ListSelect = random.randint(1, 5)
            if ListSelect == 1:
                ListIndex = random.randint(0, 25)
                char = AlphaLower[ListIndex]
                NewPassword = NewPassword + char
            if ListSelect == 2:
                ListIndex = random.randint(0, 25)
                char = AlphaUpper[ListIndex]
                NewPassword = NewPassword + char 
            if ListSelect == 3:
                ListIndex = random.randint(0, 9)
                char = Numbers[ListIndex]
                NewPassword = NewPassword + char
            if ListSelect == 4:
                ListIndex = random.randint(0, 17)
                char = UnshiftSymbols[ListIndex]
                NewPassword = NewPassword + char
            if ListSelect == 5:
                ListIndex = random.randint(0, 10)
                char = ShiftSymbols[ListIndex]
                NewPassword = NewPassword + char
        print(NewPassword)
    cont = input("Do you want to generate another password? (Y/N, case sensitive): ")
