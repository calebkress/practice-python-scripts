# Checks if a string ends with a '!', and returns the string in all caps if it does.
str = raw_input("Enter your string: ")
if str[len(str) - 1] == '!':
    print(str.upper())
else:
    print(str.lower())
