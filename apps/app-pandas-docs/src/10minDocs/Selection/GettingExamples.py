import pandas as pd
import numpy as np

dates = pd.date_range('20130101', periods=6)
print("\ndates:")
print(dates)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print("\ndf:")
print(df)
print("\ndf['A']:")
print(df['A'])
print("\ndf[0:3]:")
print(df[0:3])
print("\ndf['20130102':'20130104']:")
print(df['20130102':'20130104'])
