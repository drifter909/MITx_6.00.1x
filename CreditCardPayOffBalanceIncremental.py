balance = 3329
annualInterestRate = .2


totalPaid = 0
monthlyPayment = 10
originalBalance = balance



while balance > 0:
    balance = originalBalance
    monthlyPayment += 10
    for month in range(1,13):
        totalPaid += monthlyPayment
        balance = round(((balance - monthlyPayment)*(1+annualInterestRate/12)),2)
print "Lowest Payment:",monthlyPayment