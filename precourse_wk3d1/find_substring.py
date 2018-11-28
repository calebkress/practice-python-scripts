# Returns all positions of words in a string containing a substring
def find_substring(str=raw_input('Enter your string: '), substr=raw_input('Enter your substring: ')):
    str_list = str.split(' ')
    result = [str_list.index(i) for i in str_list if substr in i]
    return result
print(find_substring())
