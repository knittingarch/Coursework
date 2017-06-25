def gcdIter(a, b):
	
	gcd = 0
	longest_int = 0
	
	if a > b:
		longest_int = a
	else:
		longest_int = b

	for n in range(1, longest_int + 1):
		if a % n == 0 and b % n == 0:
			gcd = n
		else:
			print('no common denominator')
	
	print('The gcd for ' + str(a) + ' and ' + str(b) + ' is: ' + str(gcd) + '.')
    

gcdIter(2, 6)