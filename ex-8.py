# Ex-10
# Write a function isPrime, that takes a number as argument.
# Returns true if it is a prime number, false if it is not.
# Eg: is_prime(20) -> False, is_prime(13) -> True
import math

def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0: 
                return False
        return True
    return False

print(is_prime(20))
print(is_prime(13))