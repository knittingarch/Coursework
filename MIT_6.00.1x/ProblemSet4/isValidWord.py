def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    hand2 = dict(hand)
    
    if word in wordList:
    	for ch in word:
    		if ch in hand2:
    			hand2[ch] -= 1
    			if hand2[ch] == 0:
    			    del hand2[ch]
    		else:
    		    return False
    	return True
    else:
    	return False

# I need to check that each letter in the word guessed by the player
# is in the hand, not that each hand letter has been used

def isValidWord(word, hand, wordList):
    hand2 = dict(hand)
    if word in wordList:
    	for ch in word:
    		if ch in hand2:
    			hand2[ch] -= 1
    			if hand2[ch] < 0:
    				return False
    		else:
    		    return False
    	return True
    else:
    	return False