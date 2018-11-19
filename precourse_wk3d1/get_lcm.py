# Gets the LCM of two user inputs.
def get_lcm(num1 = input('Enter first number: '), num2 = input('Enter second number: ')):
    orig1, orig2 = num1, num2
    while num2 > 0:
        num1, num2 = num2, num1 % num2
    return (orig1 * orig2) / num1
print(get_lcm())
