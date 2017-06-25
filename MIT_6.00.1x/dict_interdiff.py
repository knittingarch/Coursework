



    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    # Your code here


def dict_interdiff(d1, d2):
	intersect = {}
	difference = {}

	for k in d1.keys():
		if k in d2.keys():
			return k

