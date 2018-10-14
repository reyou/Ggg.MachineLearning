import pandas as pd
import numpy as np

dates = pd.date_range('20130101', periods=6)
print("\ndates:")
print(dates)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print("\ndf:")
print(df)
# For getting a cross section using a label:
print("\ndf.loc[dates[0]]:")
print(df.loc[dates[0]])
# Selecting on a multi-axis by label:
print("\ndf.loc[:,['A','B']]:")
print(df.loc[:, ['A', 'B']])
# Showing label slicing, both endpoints are included:
print("\ndf.loc['20130102':'20130104',['A','B']]:")
print(df.loc['20130102':'20130104', ['A', 'B']])
# Reduction in the dimensions of the returned object:
print("\ndf.loc['20130102', ['A', 'B']]:")
print(df.loc['20130102', ['A', 'B']])
# For getting a scalar value
print("\ndf.loc[dates[0],'A']:")
print(df.loc[dates[0], 'A'])
# For getting fast access to a scalar (equivalent to the prior method):
print("\ndf.at[dates[0],'A']:")
print(df.at[dates[0], 'A'])
