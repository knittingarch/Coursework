''' A program that calculates the lowest payment necessary to pay off a balance using a Bisection Search '''

balance = 999999
annualInterestRate = 0.18


epsilon = 0.01

def createBalance(balance, annualInterestRate):	
	holder = balance
	monthInterestRate = annualInterestRate / 12.0
	lowerBound = balance / 12
	upperBound = (balance * (1 + monthInterestRate)**12) / 12.0
	payment = (lowerBound + upperBound) / 2
	
	while balance > epsilon:
		for month in range(12):
			unpaidBalance = balance - payment
			updatedBalance = unpaidBalance + (monthInterestRate * unpaidBalance)
			balance = updatedBalance
		return balance, payment, lowerBound, upperBound


def bisectSearch(balance, payment, upperBound, lowerBound):
	if 	balance < epsilon:
		balance = holder
	    upperBound = payment
	    payment = (lowerBound + upperBound) / 2
    elif balance == epsilon:
        break
	else:
	    balance = holder
	    lowerBound = payment
	    payment = (lowerBound + upperBound) / 2
		
	print('Lowest Payment: ', round(payment, 2))


balance = 320000
annualInterestRate = 0.2
monthInterestRate = annualInterestRate / 12.0

holder = balance

lowerBound = balance / 12
upperBound = (balance * (1 + monthInterestRate)**12) / 12.0
epsilon = 0.01

lowestPayment = (lowerBound + upperBound) / 2

while balance > epsilon:

	for month in range(12):
		unpaidBalance = balance - lowestPayment
		updatedBalance = unpaidBalance + (monthInterestRate * unpaidBalance)
		balance = updatedBalance

	if 	round(balance, 2) < epsilon:
		balance = holder
		upperBound = lowestPayment
		lowestPayment = (lowerBound + upperBound) / 2
	
	elif round(balance, 2) == epsilon:
	    break
	
	else:
	    balance = holder
	    lowerBound = lowestPayment
	    lowestPayment = (lowerBound + upperBound) / 2

print('Lowest Payment: ', round(lowestPayment, 2))