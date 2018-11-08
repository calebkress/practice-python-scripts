# Script to calculate a binomial distribution
import math

n = input("What is your n value? ")
k = input("What is your k value? ")
p = input("What is the probability that the event occurs? ")
perm = math.factorial(n) / math.factorial(n - k)
binomial = perm * (p ** k) * ((1 - p) ** (n - k))

print("There is a " + str(binomial) + " chance.")
