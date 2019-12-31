# Ex-6
# Read about the module random, it has method randint().
# https://docs.python.org/2/library/random.html
# Create a list with 100 random integers.

import random

integers = [random.randint(1,1000) for item in range(101) ]

print(integers)