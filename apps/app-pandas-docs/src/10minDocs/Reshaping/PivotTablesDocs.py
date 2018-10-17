import pandas as pd
import numpy as np
# See the section on Pivot Tables.
df = pd.DataFrame({'A': ['one', 'one', 'two', 'three'] * 3,
                   'B': ['A', 'B', 'C'] * 4,
                   'C': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2,
                   'D': np.random.randn(12),
                   'E': np.random.randn(12)})
print("\ndf:")
print(df)
# We can produce pivot tables from this data very easily:
pivot_table = pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C'])
print("\npivot_table:")
print(pivot_table)
