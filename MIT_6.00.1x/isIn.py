def isIn(char, aStr):
	def_string = int(len(aStr)/2)
	# if aStr == '' or char not in aStr:
	# 	return False
    if aStr == '':
        return False
    if len(aStr) == 1:
        return aStr[0] == char		
	if char == aStr[def_string]:
		return True
	elif char < aStr[def_string]:
		return isIn(char, aStr[0:def_string])
	elif char > aStr[def_string]:
		return isIn(char, aStr[def_string:])
