import pandas as pd
import numpy as np
rng = pd.date_range('1/1/2012', periods=5, freq='M')
print("\nrng:")
print(rng)
ts = pd.Series(np.random.randn(len(rng)), index=rng)
print("\nts:")
print(ts)
ps = ts.to_period()
print("\nps:")
print(ps)
time_stamp = ps.to_timestamp()
print("\ntime_stamp:")
print(time_stamp)
