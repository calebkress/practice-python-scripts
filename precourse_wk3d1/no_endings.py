# Removes all words not ending in a given letter from a given string.
def no_endings(str=raw_input('Enter a string: '), letter=raw_input('Enter the letter to find: ')):
    str_list = str.split(' ')
    result = [word for word in str_list if word.endswith(letter)]
    return result
print(no_endings())
