# Recursive attempt without monthly loop :/

# def debtPay(balance, annualInterestRate, monthlyPaymentRate):
# 	months = 12	
# 	monthInterestRate = annualInterestRate / 12.0

# 	def minPayment(monthlyPaymentRate, balance): 
# 		return monthlyPaymentRate * balance
	
# 	def unpaidBalance(balance, minPayment):
# 		return balance - minPayment
	
# 	def updatedBalance(unpaidBalance, monthInterestRate):
# 		month -= 1
# 		return unpaidBalance + (monthInterestRate * unpaidBalance)

# 	print('Remaining balance: ', round(updatedBalance(unpaidBalance(balance, minPayment(monthlyPaymentRate, balance)), monthInterestRate), 2))


# debtPay(42, 0.2, 0.04)


monthInterestRate = annualInterestRate / 12.0
for month in range(1, 13):
	minPayment = monthlyPaymentRate * balance
	unpaidBalance = balance - minPayment
	updatedBalance = unpaidBalance + (monthInterestRate * unpaidBalance)
	balance = updatedBalance
print('Remaining balance: ', round(updatedBalance, 2))