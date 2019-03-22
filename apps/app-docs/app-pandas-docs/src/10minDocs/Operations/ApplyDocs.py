import pandas as pd
import numpy as np

dates = pd.date_range('20130101', periods=6)
print("\n dates:")
print(dates)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print("\n df:")
print(df)
# Applying functions to the data:
print("\n df.apply(np.cumsum):")
print(df.apply(np.cumsum))
