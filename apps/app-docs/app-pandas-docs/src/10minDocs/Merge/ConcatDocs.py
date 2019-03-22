import pandas as pd
import numpy as np
"""
pandas provides various facilities for easily combining together 
Series, DataFrame, and Panel objects with various kinds of 
set logic for the indexes and relational algebra functionality 
in the case of join / merge-type operations.
See the Merging section.
Concatenating pandas objects together with concat():
"""
df = pd.DataFrame(np.random.randn(10, 4))
print("\ndf:")
print(df)
# break it into pieces
pieces = [df[:3], df[3:7], df[7:]]
print("\npieces:")
print(pieces)
print("\npd.concat(pieces):")
print(pd.concat(pieces))
