# Prints all divisors of a user input number.
def print_divisors(n = input('Find all divisors of: ')):
    result = []
    for i in range(n, 0, -1):
        if n % i == 0:
            result.append(i)
    return result
print(print_divisors())
