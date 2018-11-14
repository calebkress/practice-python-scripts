# Checks if a user input is a prime number
num = input('Enter a number to see if it\'s prime: ')
for i in range(2, num - 1):
    if num % i == 0:
        print('{} is not prime.').format(num)
        break
print('{} is prime.').format(num)
