import pandas as pd
import numpy as np

"""
Series is equipped with a set of string processing methods in 
the str attribute that make it easy to operate on each 
element of the array, as in the code snippet below. 
Note that pattern-matching in str generally uses regular expressions 
by default (and in some cases always uses them). See more at 
Vectorized String Methods.
"""
s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
print("\ns:")
print(s)
print("\ns.str.lower():")
print(s.str.lower())
