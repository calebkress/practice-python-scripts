# Capitalizes every other letter in a string.
str = raw_input('Enter your sentence: ')
result = ''
for i, char in enumerate(str):
    if i % 2 == 0:
        result += char.upper()
    else:
        result += char
print(result)
