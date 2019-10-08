from initialization import initialization
from eval import zero_sort, zero_normalize
from target import Target_Function

import random


t = Target_Function()

"""

The best fitness value:  0.00679775958431883
The best chromosome found:  
The best fitness value:  0.0030289165932207126
The best chromosome found:  
The best fitness value:  0.0009409885072922194
The best chromosome found:  
The best fitness value:  0.004088286518103253
The best chromosome found:  
The best fitness value:  0.0015199236733704547
The best chromosome found:  
The best fitness value:  0.001491735245865385
The best chromosome found:  
The best fitness value:  -0.00026429751019468157

"""
test = [
	[1.7081696888981952, -0.004071622306904388, 2.2179310058800086],
	[-0.051811498349913165, 0.05961634497531776, 0.3141074765481422],
	[0.08746436744448882, 0.013693531841619588, 0.2996569078423601],
	[0.003255976100151159, 0.08408257087599047, 0.29843308207284025],
	[0.03901019837038611, 0.012179166761833393, 2.5445632209257685],
	[0.002193333752714466, 0.10144418432599256, 0.062089439440717875],
	[-0.07970477408900045, -0.011100476403015591, 0.12789714496222349]
]

for g in test:
	print(t.target_value(g))
