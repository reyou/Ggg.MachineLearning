import pandas as pd
import numpy as np
rng = pd.date_range('3/6/2012 00:00', periods=5, freq='D')
print("\nrng:")
print(rng)
ts = pd.Series(np.random.randn(len(rng)), rng)
print("\nts:")
print(ts)
ts_utc = ts.tz_localize('UTC')
print("\nts_utc:")
print(ts_utc)
# Converting to another time zone:
another_time_zone = ts_utc.tz_convert('US/Eastern')
print("\nanother_time_zone:")
print(another_time_zone)
