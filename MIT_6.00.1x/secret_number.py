'''  A program that tries to guess a user's inputted number using a Bisection algorithm '''

secret_number = int(input("Please think of a number between 0 and 100! "))

high = 100
low = 0

guess = (high + low) / 2
attempts = 0

while guess != secret_number:
	print("Is your secret number", guess, "?")
	response = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
	if response == 'h':
		high = guess
		guess = round((high + low) / 2)
		attempts += 1
	elif response == 'l':
		low = guess
		guess = round((high + low) / 2)
		attempts += 1
	else:
		print("Sorry, I did not understand your input.")

while guess == secret_number:
	print("Is your secret number", guess, "?")
	response = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")		
	if response == 'c':
		print('Game over. Your secret number was:', guess)
		break
	else:
		print("Sorry, I did not understand your input.")