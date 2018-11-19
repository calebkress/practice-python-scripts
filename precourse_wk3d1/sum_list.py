# Computes the sum of a user-input list.
def sum_list(user_str = raw_input('Enter a list of numbers in the format "1, 2, 3, ...": ')):
    user_list = user_str.split(', ')
    result = 0
    for item in user_list:
        result += int(item)
    return result
print(sum_list())
