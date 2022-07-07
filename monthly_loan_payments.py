import numpy as np

#Method used for calculating the Monthly Loan Payments

calc_monthly_payment_rate = np.pmt(rate = 0.07/12, nper=5*12, pv=100000, fv=0)

#Amount to pay back monthly to achieve 
print("Monthly Payment : ",calc_monthly_payment_rate)

#Periodic deposits to achieve a specified future balance
periodic_deposit = np.pmt(rate = 0.10/12, nper=5*12, pv=0, fv = 500000)

print("Periodic Deposit : ",periodic_deposit)

