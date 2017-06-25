def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    hand2 = dict(hand)
    for ch in word:
	    if ch in hand2:
    		hand2[ch] -= 1
    		if hand2[ch] == 0:
    			del hand2[ch]
    hand = hand2
    return hand