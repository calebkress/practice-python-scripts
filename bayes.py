# Calculates P(A|B) from user input data

a = float(raw_input("What is the probability of event A? "))
b = float(raw_input("What is the probability of event B? "))
b_given_a = float(raw_input("What is the probability of event B, given event A? "))
a_given_b = (b_given_a * a) / b
print("The probability of event A, given event B, is " + str(a_given_b) + ".")
