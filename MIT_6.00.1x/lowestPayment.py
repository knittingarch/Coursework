def lowestPay(balance, annualInterestRate):
	monthInterestRate = annualInterestRate / 12.0
	def lowestPayment(amount):
		return amount
	def unpaidBalance(balance, lowestPayment):
		return balance - lowestPayment
	def updatedBalance(unpaidBalance, monthInterestRate):
		return unpaidBalance + (monthInterestRate * unpaidBalance)

	print('Lowest Payment:', round(lowestPayment(),0))


lowestPay(3329, 0.2)



balance = 4773
holder = balance
annualInterestRate = 0.2
monthInterestRate = annualInterestRate / 12.0

lowestPayment = 370
while balance != 0:

	for month in range(1, 13):
		unpaidBalance = balance - lowestPayment
		updatedBalance = unpaidBalance + (monthInterestRate * unpaidBalance)
		balance = updatedBalance

	if updatedBalance <= 0:
		print('Lowest Payment: ', lowestPayment)
		break	
	else:
	    balance = holder
	    lowestPayment += 10