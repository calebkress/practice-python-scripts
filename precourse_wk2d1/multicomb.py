# A tool for calculating multi-step combinations
import math

steps = input("How many steps of combination are there? ")
result = 1
for x in range(0, steps):
    n = input("What is your n value for step " + str(x + 1) + "? ")
    k = input("What is your k value for step " + str(x + 1) + "? ")
    comb = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
    result = result * comb
print("The result is " + str(result) + ".")
