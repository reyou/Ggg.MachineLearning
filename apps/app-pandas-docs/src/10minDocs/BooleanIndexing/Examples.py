import pandas as pd
import numpy as np

dates = pd.date_range('20130101', periods=6)
print("\ndates:")
print(dates)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print("\ndf:")
print(df)
# Using a single column’s values to select data.
print("\ndf[df.A > 0]:")
print(df[df.A > 0])
# Selecting values from a DataFrame where a boolean condition is met.
print("\ndf[df > 0]:")
print(df[df > 0])
# Using the isin() method for filtering:
df2 = df.copy()
df2['E'] = ['one', 'one', 'two', 'three', 'four', 'three']
print("\ndf2:")
print(df2)
print("\ndf2[df2['E'].isin(['two', 'four'])]:")
print(df2[df2['E'].isin(['two', 'four'])])
