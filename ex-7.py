# Ex-8
# Read about the module random, it has method randint().
# https://docs.python.org/2/library/random.html
# Create a list with 100 random integers.
# Find out the frequency (how many times each integers is repeated in the list)
# Output should be a dictionary key as the random integer and value is the frequency
# Eg: random_integers_list = [1,2,3,4,1,3,6]
# outputs: frequencies = {1:2, 2:1, 3:2, 4: 1, 6: 1}

import random

def generate_random_numbers():
    return [random.randint(1,10) for item in range(101)]

random_numbers = generate_random_numbers()

uniques = set(random_numbers)

frequencies = {}

for unique in uniques:
    frequencies[unique] = random_numbers.count(unique)

print(frequencies)
