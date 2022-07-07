import numpy as npf

"""
You invest 1000 for 5 years an a yearly return of 8%
    @FutureValueOfAnInvestment
hence : 
        Year 1 = 1000 + 8%
        Year 2 = Year 1 + 8%
        Year 3 = Year 2 + 8%
        Year 4 = Year 3 + 8%
        Year 5 = Year 4 + 8%
"""
#Calculate how much you'll have after 5 years

Years = int(input("Please Enter the number of years\n"))

Am = int(input("Please Enter the amount\n"))
Amount = Am * -1

Per = float(input("Please Enter the number the percentage e.g. (0.05)\n"))

PeriodicPayments = float(input("Please Enter the amount\n"))

result = npf.fv(rate = Per, nper = Years, pmt = 0, pv = Amount)

print(result)

"""

The Code - 
    nper = number of periods/Year
    pv = present value (investment amount is subtracted since we are the ones that add it in)
    pmt =   periodic payments corresponds to investments/payments in our case its zero
            payment against loan principle plus interest.

"""




