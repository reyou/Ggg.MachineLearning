import pandas as pd
import numpy as np

dates = pd.date_range('20130101', periods=6)
print("\ndates:")
print(dates)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print("\ndf:")
print(df)
# Reindexing allows you to change/add/delete the index on a specified axis.
# This returns a copy of the data.
df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])
df1.loc[dates[0]:dates[1], 'E'] = 1
print("\ndf1:")
print(df1)
# To drop any rows that have missing data.
df3 = df1.dropna(how='any')
print("\ndf3:")
print(df3)
# Filling missing data.
df3 = df1.fillna(value=5)
print("\ndf3:")
print(df3)
# To get the boolean mask where values are nan.
df3 = pd.isna(df1)
print("\ndf3:")
print(df3)
