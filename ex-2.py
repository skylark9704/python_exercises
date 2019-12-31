# Ex-2
# Write a function say_hello which takes arbitrary number of names as argument
#and prints hello, <name>

def say_hello(*args):
    for item in args:
        print("Hello, {}".format(item))
    print('\n')
    
say_hello('goutham')

# Output: Hello, goutham

say_hello('goutham','ng','pg')

# Output:
# Hello, goutham
# Hello, ng
# Hello, pg
