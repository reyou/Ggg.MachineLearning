import pandas as pd
import numpy as np
# Append rows to a dataframe. See the Appending section.

df = pd.DataFrame(np.random.randn(8, 4), columns=['A', 'B', 'C', 'D'])
print("\ndf:")
print(df)
s = df.iloc[3]
print("\ns:")
print(s)
appended = df.append(s, ignore_index=True)
print("\nappended:")
print(appended)
