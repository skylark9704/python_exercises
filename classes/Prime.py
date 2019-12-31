import math

class Prime:
	""" A simple class for obtaining prime numbers"""

	def get_all_primes(self,number):
		""" Gets all prime numbers upto specified number given in argument"""
		primes = []
		gen = self._get_prime(1)
		for _ in range(number + 1):
			primes.append(gen.next())
		return primes
	
	def next_prime(self,number):
		""" Gets the next closest prime number from the specified number given in argument"""
		if number <= 1:
			return 2
		
		else:
			gen = self._get_prime(number)
			prime = gen.next()
			if prime == number:
				return gen.next()
			return prime

	def previous_prime(self,number):
		""" Gets the previous closest prime number from the specified number given in argument"""
		if number <= 2:
			return 2
		else:
			gen = self._get_prime(number,0)
			prime = gen.next()
			if prime == number:
				return gen.next()
			return prime

	def nth_prime(self,nth):
		""" Gets the nth prime number specified in argument"""
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