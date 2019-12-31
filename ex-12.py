# Ex-12
# Write a class Prime.
# It supports the following operations:
# Check out this article to find primes in an optimized way.
# http://stackoverflow.com/a/5813926/2131120

import math

class Prime:

    def getallprimes(self,number):
        primes = []
        gen = self._get_prime(1)
        for _ in range(number + 1):
            primes.append(gen.next())
        return primes
    
    def nextprime(self,number):
        if number <= 1:
            return 2
        
        else:
            gen = self._get_prime(number)
            prime = gen.next()
            if prime == number:
                return gen.next()
            return prime

    def previousprime(self,number):
        if number <= 2:
            return 2
        else:
            gen = self._get_prime(number,0)
            prime = gen.next()
            if prime == number:
                return gen.next()
            return prime

    def nthprime(self,nth):
        gen = self._get_prime(1)
        for x in range(nth + 1):
            prime = gen.next()
            if(x == nth):
                return prime
            

    def _get_prime(self,number,mode = 1):
        while True:
            if self._is_prime(number):
                yield number
            if mode == 1:
                number += 1
            else:
                number -= 1

    def _is_prime(self,number):
        if number > 1:
            if number == 2:
                return True
            if number % 2 == 0:
                return False
            for x in range(3, int(math.sqrt(number) + 1), 2):
                if number % x == 0: 
                    return False
            return True
        return False

""" p = Prime()
p.nthprime(100) # prints 100th prime
p.nextprime(2) # 3. It should return 2 for all numbers <= 1
p.previousprime(3) # 2. It should return 2 for all numbers <=2
p.getallprimes(10)  """# 2, 3, 5, 7

p = Prime()
print(p.nthprime(10))
print(p.getallprimes(10))
print(p.nextprime(5))
print(p.previousprime(5))


