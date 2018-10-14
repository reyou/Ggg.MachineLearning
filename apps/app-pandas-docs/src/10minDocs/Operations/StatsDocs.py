import pandas as pd
import numpy as np

dates = pd.date_range('20130101', periods=6)
print("\ndates:")
print(dates)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print("\ndf:")
print(df)
# Performing a descriptive statistic:
print("\ndf.mean():")
print(df.mean())
# Same operation on the other axis:
print("\ndf.mean(1):")
print(df.mean(1))
"""Operating with objects that have different dimensionality and need alignment. 
In addition, pandas automatically broadcasts along the specified dimension.
"""
s = pd.Series([1, 3, 5, np.nan, 6, 8], index=dates).shift(2)
print("\ns:")
print(s)
print("\ndf.sub(s, axis='index'):")
print(df.sub(s, axis='index'))
