# Takes a list of numbers and an integer, and returns an array saying whether each number in the list is divisible by the second number.
def yes_no(num_str = raw_input('Enter a list of comma-separated numbers: '), num = input('Enter a number to divide by: ')):
    num_list = num_str.split(', ')
    print(num_list)
    result = ['yes' if int(i) % num == 0 else 'no' for i in num_list]
    return result
print(yes_no())
