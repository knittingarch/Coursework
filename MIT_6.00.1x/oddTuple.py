def oddTuple(aTup):
	newTup = ()
	for x in range(len(aTup)):
		if x % 2 == 0:
			newTup += (aTup[x],)
	return newTup

oddTuple(('I', 'am', 'a', 'test', 'tuple'))