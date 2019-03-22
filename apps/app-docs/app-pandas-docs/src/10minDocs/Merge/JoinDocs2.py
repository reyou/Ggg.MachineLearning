import pandas as pd
import numpy as np
# Another example that can be given is:.
left = pd.DataFrame({'key': ['foo', 'bar'], 'lval': [1, 2]})
print("\nleft:")
print(left)
right = pd.DataFrame({'key': ['foo', 'bar'], 'rval': [4, 5]})
print("\nright:")
print(right)
merged = pd.merge(left, right, on='key')
print("\nmerged:")
print(merged)
