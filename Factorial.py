num1 = int(input("Enter a number: "))
count = 1
factorial = 1
if num1 <= 0:
    print("You cannot have 0 or negative values")
else:
    while count <= num1:
        factorial = count*factorial
        count += 1
    print(factorial)