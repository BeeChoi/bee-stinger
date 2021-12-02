numInputs = int(input("How many numbers do you want in your list? "))
nums = []
for i in range (numInputs):
  num = int(input("Enter a number here: "))
  nums.append(num)
print(nums)  
print(sum(nums))
