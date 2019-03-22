import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dates = pd.date_range('20130101', periods=6)
#
"""Two-dimensional size-mutable, potentially heterogeneous tabular data structure with 
labeled axes (rows and columns). Arithmetic operations align on both row and column 
labels. Can be thought of as a dict-like container for Series objects. The primary 
pandas data structure."""
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print("df:", type(df))
print(df)
