from time import sleep
print("Hello, and welcome to a very cool calculator")
sleep(0.5)
num1 = float(input("What is your first number? "))
sleep(0.5)
num2 = float(input("What is your second number? "))

multiplication = num1*num2
addition = num1+num2
division = num1/num2
subtraction = num1-num2
division2 = num2/num1
subtraction2 = num2-num1
exp1 = num1**2
exp2 = num2**2
sqrt1 = num1**.5
sqrt2 = num2**.5

multiplication = format(multiplication, ',.3f')
addition = format(addition, ',.3f')
division = format(division, ',.3f')
subtraction = format(subtraction, ',.3f')
division2 = format(division2, ',.3f')
subtraction2 = format(subtraction2, ',.3f')
exp1 = format(exp1, ',.3f')
exp2 = format(exp2, ',.3f')
sqrt1 = format(sqrt1, ',.3f')
sqrt2 = format(sqrt2, ',.3f')

print("-----------------------------")
print(str(num1) + " + " + str(num2) + " =", addition)
print("-----------------------------")
print(str(num1) + " - " + str(num2) + " =", subtraction)
print("-----------------------------")
print(str(num1) + " * " + str(num2) + " =", multiplication)
print("-----------------------------")
print(str(num1) + " / " + str(num2) + " =", division)
print("-----------------------------")
print(str(num2) + " + " + str(num1) + " =", division2)
print("-----------------------------")
print(str(num2) + " - " + str(num1) + " =", subtraction2)
print("-----------------------------")
print(str(num1) + "^2 " + " =", exp1)
print("-----------------------------")
print(str(num2) + "^2 " + " =", exp2)
print("-----------------------------")
print("Square Root of " + str(num1) + " =", sqrt1)
print("-----------------------------")
print("Square Root of " + str(num2) + " =", sqrt2)
print("-----------------------------")