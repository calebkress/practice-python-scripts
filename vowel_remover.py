# Removes all vowels from a given string
vowels = ['a', 'e', 'i', 'o', 'u']
str = raw_input('Enter your sentence: ')
no_vowels = ''.join(char for char in str if char not in vowels)
print(no_vowels)
