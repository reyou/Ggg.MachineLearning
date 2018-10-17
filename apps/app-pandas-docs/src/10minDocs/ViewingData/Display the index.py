import numpy as np
import pandas as pd


dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print("df.index:")
print(df.index, "\n")
print("df.columns:")
print(df.columns, "\n")
print("df.values:")
print(df.values, "\n")
print("df.describe:")
print(df.describe())

# Transposing your data
print("\nTransposing your data:")
print(df.T)

# Sorting by an axis
print("\nSorting by an axis:")
print(df.sort_index(axis=1, ascending=False))

# Sorting by values
print("\nSorting by values:")
print(df.sort_values(by='B'))
