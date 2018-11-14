# Calculates the factorial of a user-input number
num = input("Calculate the factorial of what number? ")
orig = num
result = 1
for x in range(1, num + 1):
    result *= x
print("The factorial of {} is {}.").format(orig,result)
