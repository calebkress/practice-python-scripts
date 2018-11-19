# Computes the product of items in a user-input list.
def list_product(user_str = raw_input('Enter a list of numbers in the format "1, 2, 3, ...": ')):
    user_list = user_str.split(', ')
    result = 1
    for item in user_list:
        result *= int(item)
    return result
print(list_product())
