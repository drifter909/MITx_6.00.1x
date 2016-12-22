balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
totalPaid = 0
monthlyPayment = 0

for month in range(1,13):
    monthlyPayment = round(monthlyPaymentRate*balance,2)
    totalPaid += monthlyPayment
    balance = round(((balance - monthlyPayment)*(1+annualInterestRate/12)),2)
    print "Month: ", month
    print "Minimum monthly payment: ", monthlyPayment
    print "Remaining balance: ", balance
print "Total paid: ",totalPaid
print "Remaining balance: ", balance