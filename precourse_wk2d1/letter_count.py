# Counts the number of times a given letter appears in a given string.
str = raw_input('Enter a string: ')
letter = raw_input('What letter am I looking for? ')
count = 0
for char in str:
    if char.lower() == letter.lower():
        count += 1
print('The letter {} occurs in the string {} times.').format(letter,count)
