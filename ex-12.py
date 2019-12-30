# Ex-12
# Write a class Prime.
# It supports the following operations:
# Check out this article to find primes in an optimized way.
# http://stackoverflow.com/a/5813926/2131120

p = Prime()
p.nthprime(100) # prints 100th prime
p.nextprime(2) # 3. It should return 2 for all numbers <= 1
p.previousprime(3) # 2. It should return 2 for all numbers <=2
p.getallprimes(10) # 2, 3, 5, 7

