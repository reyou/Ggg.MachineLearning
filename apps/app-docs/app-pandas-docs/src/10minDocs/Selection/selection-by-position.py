import pandas as pd
import numpy as np

dates = pd.date_range('20130101', periods=6)
print("\ndates:")
print(dates)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print("\ndf:")
print(df)
# Select via the position of the passed integers:
print("\ndf.iloc[3]:")
print(df.iloc[3])
# By integer slices, acting similar to numpy/python:
print("\ndf.iloc[3:5,0:2]:")
print(df.iloc[3:5, 0:2])
# By lists of integer position locations, similar to the numpy/python style:
print("\ndf.iloc[[1,2,4],[0,2]]:")
print(df.iloc[[1, 2, 4], [0, 2]])
# For slicing rows explicitly:
print("\ndf.iloc[1:3,:]:")
print(df.iloc[1:3, :])
# For slicing columns explicitly:
print("\ndf.iloc[:,1:3]:")
print(df.iloc[:, 1:3])
# For getting a value explicitly:
print("\ndf.iloc[1,1]:")
print(df.iloc[1, 1])
# For getting fast access to a scalar (equivalent to the prior method):
print("\ndf.iat[1,1]:")
print(df.iat[1, 1])
