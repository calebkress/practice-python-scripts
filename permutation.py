# Calculates the number of permutations (order matters) from a set
import math

n = input("How many objects are there in total? ")
k = input("How big a subset are you creating? ")
perm = math.factorial(n) / math.factorial(n - k)

print("There are " + str(perm) + " possible permutations.")
