import pandas as pd
import numpy as np

dates = pd.date_range('20130101', periods=6)
print("\ndates:")
print(dates)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print("\ndf:")
print(df)
# See more at Histogramming and Discretization.
s = pd.Series(np.random.randint(0, 7, size=10))
print("\ns:")
print(s)
print("\ns.value_counts():")
print(s.value_counts())
