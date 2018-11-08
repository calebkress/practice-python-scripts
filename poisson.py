# Calculates a poisson distribution
import math

k = input("What is your k value? ")
lamb = input("What is your lambda value? ")
poisson = math.exp(-lamb) * ((lamb ** k) / (math.factorial(k)))

print("The result is " + str(poisson) + ".")
