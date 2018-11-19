# Counts the number of words in a string.
def word_count(str = raw_input('Enter your string: ')):
    words = str.split(' ')
    return(len(words))
print('There are {} words in your string.').format(word_count())
