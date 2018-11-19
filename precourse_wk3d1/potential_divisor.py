# Takes a number and a potential divisor; returns True/False
def potential_divisor(n = input('What\'s your number? '), divisor = input('What\'s your potential divisor? ')):
    return n % divisor == 0
print(potential_divisor())
