# Calculates the factorial of a user input using a function.
def get_factorial(num = int(input('Get factorial of: '))):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result
print(get_factorial())
