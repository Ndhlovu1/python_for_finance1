import numpy as np
import matplotlib.pyplot as plt


"""
PROJECT :   Analyze price of bitcoin from the array
            Calculate return on investment values,
            analyze rate return, this is a build up project, 
            eventually we will analyze data from the web

"""

#price for 2018-2021
bitcoin = [3869.47, 7188.46, 22203.31, 29391.78]

#Calculate the standard deviation of the price, refer to numDataTest
standard_deviation = np.std(bitcoin)
print("The Standard Deviation is : ", standard_deviation )

#You wanna know your IRR with machines you bought
#Your return will be 10btc per year,
"""
Hence : 10 * year 1 price 
        10 * year 2 price
        10 * year 3 price,
        10 * year 4 price
        10 * year 5 price
"""
#Price for btc
option_1 = [-500000, 38694.70, 71884.60, 222033.10, 293917.8]



#year = [2018, 2019, 2020, 2021,]
year = ["2018", "2019", "2020", "2021"]


irr_amount = np.irr(option_1)


print("Your Internal Rate of Return will be : ",irr_amount)

#Get a graph that shows how your data has grown in the chat

print("Your graph of growth")

plt.plot(year ,bitcoin)

plt.savefig('btc_money_made3.png')
print("Done")


