import pandas as pd
import numpy as np
rng = pd.date_range('1/1/2012', periods=100, freq='S')
print("\nrng:")
print(rng)
ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)
print("\nts:")
print(ts)
"""
Convenience method for frequency conversion and resampling of time series. 
Object must have a datetime-like index (DatetimeIndex, PeriodIndex, or TimedeltaIndex), 
or pass datetime-like values to the on or level keyword.
"""
resampled = ts.resample('5Min').sum()
print("\nresampled:")
print(resampled)
