import pandas as pd
import numpy as np
"""
Converting between period and timestamp enables some convenient arithmetic 
functions to be used. In the following example, we convert a quarterly 
frequency with year ending in November to 9am of the end 
of the month following the quarter end:
"""
prng = pd.period_range('1990Q1', '2000Q4', freq='Q-NOV')
print("\n prng:")
print(prng)
ts = pd.Series(np.random.randn(len(prng)), prng)
print("\n ts:")
print(ts)
ts.index = (prng.asfreq('M', 'e') + 1).asfreq('H', 's') + 9
head = ts.head()
print("\n head:")
print(head)
