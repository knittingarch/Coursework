'''  A program that tries to guess a user's inputted number using a Bisection algorithm '''

print("Please think of a number between 0 and 100!")

high = 100
low = 0

guess = (high + low) / 2
attempts = 0

response = ''

while response != 'c':
	print("Is your secret number", guess, "?")
	response = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
	if response == 'h':
		high = guess
		guess = int((high + low) / 2)
		attempts += 1
	elif response == 'l':
		low = guess
		guess = int((high + low) / 2)
		attempts += 1
	elif response == 'c':
		break
	else:
		print("Sorry, I did not understand your input.")

if response == 'c':
	print('Game over. Your secret number was:', guess)
