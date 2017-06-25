    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''

aList = [[1,'a',['cat'],2],[[[3]],'dog'],4,5] 

def flatten(aList):
	for i in aList:
		if isinstance(i, (list)):
			for j in flatten(i):
				yield j
		else:
			yield i
print(list(flatten(aList)))

