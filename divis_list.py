# Returns a list of all numbers divisible by a given number between 0 and another given number.
max = input('Search for numbers between 0 and what number? ')
divis = input('Find numbers divisible by what number? ')
result = []
for i in range(1, max):
    if i % divis == 0:
        result.append(i)
print(result)
