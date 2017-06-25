def hangman(secretWord):
	guesses_left = 8
	guessed = []
	allowedChars = 'abcdefghijklmnopqrstuvwxyz'
	allowedChars = list(allowedChars)

	print('Welcome to the game, Hangman!')
	print('I am thinking of a word that is', len(secretWord), 'letters long')
	# partial = ['_ '] * (len(secretWord) - 1) + ['_']
	partial = ['_'] * len(secretWord)

	while guesses_left and ''.join(partial) != secretWord:
		print(('-') * 11)
		print('You have', guesses_left, 'guesses left')
		print('Available letters:', ''.join(allowedChars))
		letter = input('Please guess a letter: ')
		if letter in guessed or letter in partial:
			print("Oops! You've already guessed that letter: ", ''.join(partial))
			continue
		elif letter in secretWord:
			allowedChars.remove(letter)
			guessed.append(letter)
			for index, ch in enumerate(secretWord):
				if letter == ch:
					partial[index] = ch
				else:
					if ch in partial:
						continue
					else:
						continue
			print('Good guess:', ''.join(partial))
		else:
			allowedChars.remove(letter)
			guessed.append(letter)
			print('Oops! That letter is not in my word: ', ''.join(partial))
			guesses_left -= 1
	
	if ''.join(partial) == secretWord:
		print(('-') * 11)
		print("Congratulations, you won!")
	else:
		print(('-') * 11)
		print('Sorry, you ran out of guesses. The word was ' + secretWord + '.')
