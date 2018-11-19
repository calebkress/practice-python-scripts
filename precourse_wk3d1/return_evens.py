# Takes a list of numbers and returns the even values.
def return_evens(user_str = raw_input('Enter a list of numbers in the format "1, 2, 3, ...": ')):
    user_list = user_str.split(', ')
    result = []
    for item in user_list:
        if int(item) % 2 == 0:
            result.append(item)
    return result
print(return_evens())
