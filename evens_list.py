# Prints a list of all even numbers between 0 and an input number.
max = input('Print all even numbers between 0 and what number? ')
result = []
for i in range(1, max):
    if i % 2 == 0:
        result.append(i)
print(result)
