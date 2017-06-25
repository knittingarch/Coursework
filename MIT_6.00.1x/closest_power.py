    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.

    Test Cases:
    closest_power(3,12) returns 2
	closest_power(4,12) returns 2
	closest_power(4,1) returns 0
    '''

 def closest_power(base, num):
 	result = 0
 	exp = 1
 	while base**exp < num:
 		if base**exp <= num < base**(exp+1):
 			result = exp

 		elif num - base**exp <= base**(exp + 1) - num:
 			result = exp + 1

 		exp += 1

 	return result