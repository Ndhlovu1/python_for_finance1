import numpy as np

#This project is designed to produce the internal Rate of Return
"""
Assuming that we have had made an investment of 5000 and we have received back
    500,700, 1000, 3000
    Let's find our Internal Rate of Return

Return on investment (ROI) and internal rate of return (IRR) are performance 
measurements for investments or projects.



"""

cashflow = [-5000, 500, 700, 1000, 3000]

amount_of_return = np.irr(cashflow)

print("Your IRR now is : ",amount_of_return)