''' assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    # Your code here
For example, if L = [[1, 2], [3, 4], [5, 6, 7]] then deep_reverse(L) 
mutates L to be [[7, 6, 5], [4, 3], [2, 1]]
'''

def deep_reverse(L):
    L[:] = [n[::-1] for n in L[::-1]]

deep_reverse([[1, 2], [3, 4], [5, 6, 7]])


def deep_reverse(L):
    full_reverse = []
    new_L = L[::-1]
    L[:] = [n[::-1] for n in new_L]

deep_reverse([[1, 2], [3, 4], [5, 6, 7]])


def deep_reverse(L):
    full_reverse = []
    new_L = L[::-1]
    for n in new_L:
        full_reverse.append((n[::-1]))

deep_reverse([[1, 2], [3, 4], [5, 6, 7]])