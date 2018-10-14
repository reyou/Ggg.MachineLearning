import pandas as pd
import numpy as np

dates = pd.date_range('20130101', periods=6)
print("\ndates:")
print(dates)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print("\ndf:")
print(df)
# Setting a new column automatically aligns the data by the indexes.
s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20130102', periods=6))
print("\ns1:")
print(s1)
# Setting values by label:
df.at[dates[0], 'A'] = 0
print("\ndf:")
print(df)
# Setting values by position:
df.iat[0, 1] = 0
print("\ndf:")
print(df)
# Setting by assigning with a NumPy array:
df.loc[:, 'D'] = np.array([5] * len(df))
print("\ndf:")
print(df)
# A where operation with setting.
df2 = df.copy()
df2[df2 > 0] = -df2
print("\ndf2:")
print(df2)
