# Takes two lists from user input and finds common elements
set1a = input('Enter a number for set 1: ')
set1b = input('Enter a number for set 1: ')
set1c = input('Enter a number for set 1: ')
set1d = input('Enter a number for set 1: ')
set1e = input('Enter a number for set 1: ')
set1f = input('Enter a number for set 1: ')
set1g = input('Enter a number for set 1: ')
set2a = input('Enter a number for set 2: ')
set2b = input('Enter a number for set 2: ')
set2c = input('Enter a number for set 2: ')
set2d = input('Enter a number for set 2: ')
set2e = input('Enter a number for set 2: ')
set2f = input('Enter a number for set 2: ')
set2g = input('Enter a number for set 2: ')

set1 = [set1a, set1b, set1c, set1d, set1e, set1f, set1g]
set2 = [set2a, set2b, set2c, set2d, set2e, set2f, set2g]
commons = []
print(set1, set2)

for i, el in enumerate(set1):
    for j, el in enumerate(set2):
        if set1[i] == set2[j] and set1[i] not in commons:
            commons.append(set1[i])

print('The common values are {}').format(commons)
