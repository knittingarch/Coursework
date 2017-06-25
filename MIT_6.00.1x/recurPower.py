# base**exp = base * base * base * base ... * base
# base * base * (exp-1)

# base = 2
# exp = 4

# 2**4 = 2 * 2 * 2 * 2
# 	 = 2 * (2 * (exp-1)) = 2 * 3
# 	 = 2 * 2 * (2 * 2)
# 	 = 2 * 2 * 2 * (2 *1)


def recurPower(base, exp):
	if exp <= 0:
		return 1
	else: 
		return base * recurPower(base, exp-1)

recurPower(2, 4)		