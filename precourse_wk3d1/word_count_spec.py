# Counts the number of words in a sentence, split by a given delimiter
def word_count_spec(str = raw_input('Enter your string: '), delimiter = raw_input('Enter your delimiter: ')):
    words = str.split(delimiter)
    return(len(words))
print('There are {} words in your string.').format(word_count_spec())
