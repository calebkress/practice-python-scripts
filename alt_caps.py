# Capitalizes every other letter in a string.
str = raw_input('Enter your sentence: ')
result = ''
for i, char in enumerate(str):
    print(str[i])
    if i % 2 == 0:
        str[i] = char.upper()
print(str)
