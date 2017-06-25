def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    hand_value = 0
    for k, v in hand.items():
    	hand_value += v
    return hand_value
