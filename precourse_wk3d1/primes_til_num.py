# Returns a list of all primes up to a given number.
def primes_til_num(num = input('Find all primes before what number? ')):
    result = []
    for i in range(1, num + 1):
        is_prime = True
        for j in range(2, i - 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime == True:
            result.append(i)
    return result
print(primes_til_num())
