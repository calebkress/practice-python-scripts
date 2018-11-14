# Outputs a list of multiples of a user input between zero and another user input
num = input('Find multiples of: ')
max = input('From 0 to: ')
multiples = []
for i in range(1, max):
    if num % i == 0:
        multiples.append(i)
print('The multiples of {} less than {} are {}.').format(num, max, multiples)
