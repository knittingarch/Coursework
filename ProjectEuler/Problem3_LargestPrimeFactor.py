# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

# Pseudo code
# write a function that identifies the prime numbers from 1 to number
# create an empty list
# take a number and divide it by 2 until a prime number is left
# append that number to the list
# divide the number by each prime number
# return the largest prime that divides evenly into the number

primes = []

def largestPrimeFactor(n):
	# for i in range(n):
	if n % 2 == 0:
		n = n / 2
	elif n == 2:
		primes.append(n)
	else:
		primes.append(n)
	print primes

largestPrimeFactor(11)
