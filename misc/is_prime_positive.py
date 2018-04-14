import math

def is_prime_positive(num):

    if num == 2:
        return True

    if num <= 0 or num == 1 or num % 2 == 0:
        return False
    else:
        sqr = int(math.sqrt(num)) + 1
        for divisor in range(3, sqr, 2):
            if num % divisor == 0:
                return False
        return True

print(is_prime_positive(1))
print(is_prime_positive(-10))
print(is_prime_positive(2))
print(is_prime_positive(0))
print(is_prime_positive(31))
print(is_prime_positive(15))
print(is_prime_positive(17))