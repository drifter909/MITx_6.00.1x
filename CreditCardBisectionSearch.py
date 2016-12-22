balance = 999999
annualInterestRate = 0.18
low_bound = balance / 12
high_bound = balance*(((annualInterestRate / 12) + 1)**12)
original_balance = balance
completed = False

while abs(balance) >= .01:
    totalPaid = 0
    balance = original_balance
    for month in range(1,13):
        monthlyPayment = (high_bound + low_bound) / 2 
        totalPaid += monthlyPayment
        balance = round(((balance - monthlyPayment)*(1+annualInterestRate/12)),2)
    if balance > 0:
        low_bound = (high_bound + low_bound) / 2
    if balance < 0:
        high_bound = (high_bound + low_bound) / 2

print "Lowest Payment:",round(monthlyPayment,2)
    