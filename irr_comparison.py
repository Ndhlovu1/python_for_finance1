import numpy as np

#Compare the IRR for the same periods of time but of 2 opportunities

opportunity_1 = [-50000, 10000, 25000, 25000, 35000, 42000]

opportunity_2 = [-30000, 10000, 13000, 18000, 25000, 20000]

opp1 = np.irr(opportunity_1)
opp2 = np.irr(opportunity_2)

print("Opportunity 1 : ", opp1)
print("Opportunity 2 : ", opp2)



