# Calculates the number of combinations (order doesn't matter) from a set
import math

n = input("How many objects are there in total? ")
k = input("How big a subset are you creating? ")
comb = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))

print("There are " + str(comb) + " possible combinations.")
