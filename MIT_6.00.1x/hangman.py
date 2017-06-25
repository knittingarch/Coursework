
import random
import string

def hangman():
	f = open('/hangman/words.txt', 'r')
	words = []
	for line in f.readlines():
		for word in line.split(' '):
			words.append(word)
	f.close()
	return words

def pick_a_word(words):
	selected_word = random.choice(words)
	return selected_word

print('Your selected word is', len(selected_word), 'letters.')


def guess_letters(word):
	guesses_left = 8
	guessed = []
	allowedChars = 'abcdefghijklmnopqrstuvwxyz'
	partial = []
	
	print('I am thinking of a word that is', len(word), 'long.')
	for g in range(guesses_left):
					print('You have', guesses_left, 'guesses left.')
guess = input('Please guess one letter:')
		while len(guess) != 1 or guess not in allowedChars:
			guess = input('Please guess a letter:')
		if guess in word:
			for index, ch in enumerate(word):
				if ch in partial:
					pass
				if ch != guess:
					ch = '_'
					partial.append(ch)
				else:
					partial.append(ch)
			if guess in guessed:
				print('Sorry, you already guessed that one.')
				guess = input('Please guess another letter:')
			guessed.append(guess)
			num_letters_in_word = word.count(guess)
			print('There are', num_letters_in_word, 'in the selected word.')
			print('So far, you have guessed the following letters:', guessed)
		else:
			guessed.append(guess)
			print('Sorry.', guess.upper(), 'is not in the word.')
			print('So far, you have guessed the following letters:', guessed)
			guesses_left -= 1
			print('You have', guesses_left, 'guesses left.')
	print("This round's word was", word, "!")
