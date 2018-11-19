# Checks if a user input is a prime number using a function.
def is_prime(num = int(input('Enter a number to check if it\'s prime: '))):
    is_prime = True
    for i in range(2, num - 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime == True:
        print('{} is prime.').format(num)
    else:
        print('{} is not prime.').format(num)
is_prime()
