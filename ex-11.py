# Ex-13
# Accomplish the following using string slicing
# Print excluding first 2 characters
# Print first 4 characters
# Print every alternate letter
# Reverse the string
animal = 'elephant'

print(animal[2:])
print(animal[:4])
print(''.join([letter for letter in animal if(animal.index(letter) % 2 == 0)]))
print(''.join(reversed(animal)))
