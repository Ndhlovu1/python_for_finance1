import numpy as np

"""

PV =    Present Value of an investment - Calculate how much you'd have to invest today
        inorder to reach a particular amount hence declare it in the future value(fv) tab
        It'll also be based on the amount and the years to reach the goal
"""

present_value = np.pv(rate = 0.10, nper=8, pmt = 0, fv=1000)

print("Future Value is :", present_value)


