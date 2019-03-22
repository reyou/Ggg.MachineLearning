import pandas as pd
import numpy as np
# SQL style merges. See the Database style joining section.
left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})
print("\nleft:")
print(left)
right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})
print("\nright:")
print(right)
merged = pd.merge(left, right, on='key')
print("\nmerged:")
print(merged)
