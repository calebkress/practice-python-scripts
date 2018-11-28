# Takes a string and returns a list of each word length.
def word_lengths(str = raw_input('Enter your string: '), delimiter = raw_input('Enter your delimiter: ')):
    str_list = str.split(delimiter)
    result = [len(item) for item in str_list]
    return result
print(word_lengths())
