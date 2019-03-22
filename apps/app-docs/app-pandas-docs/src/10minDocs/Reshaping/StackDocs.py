import pandas as pd
import numpy as np
# http://pandas.pydata.org/pandas-docs/stable/10min.html#stack
# See the sections on Hierarchical Indexing and Reshaping.
"""
Return a zip object whose .next() method returns a tuple where the i-th 
element comes from the i-th iterable argument. The .next() method continues until 
the shortest iterable in the argument sequence is exhausted and then it 
raises StopIteration.
"""
tuples = list(zip(*[['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],
                    ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]))
print("\ntuples:")
print(tuples)
index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
print("\nindex:")
print(index)
df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=['A', 'B'])
print("\ndf:")
print(df)
df2 = df[:4]
print("\ndf2:")
print(df2)
# The stack() method “compresses” a level in the DataFrame’s columns.
stacked = df2.stack()
print("\nstacked:")
print(stacked)
"""
With a “stacked” DataFrame or Series (having a MultiIndex as the index), 
the inverse operation of stack() is unstack(), which by default unstacks 
the last level:
"""
unstacked = stacked.unstack()
print("\nunstacked:")
print(unstacked)
unstacked1 = stacked.unstack(1)
print("\nunstacked1:")
print(unstacked1)
unstacked0 = stacked.unstack(0)
print("\nunstacked0:")
print(unstacked0)
