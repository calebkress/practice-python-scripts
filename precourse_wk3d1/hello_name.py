# Takes a name and returns 'Hello, {name}!'
def hello_name(name = raw_input('What\'s your name? ')):
    return('Hello, {}!').format(name)
print(hello_name())
