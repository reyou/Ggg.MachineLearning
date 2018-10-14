import pandas as pd
import numpy as np

dates = pd.date_range('20130101', periods=6)
print("\ndates:")
print(dates)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print("\ndf:")
print(df)
# Applying functions to the data:
print("\ndf.apply(np.cumsum):")
print(df.apply(np.cumsum))
