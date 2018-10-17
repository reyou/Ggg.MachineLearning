"""
* http://pandas.pydata.org/pandas-docs/stable/10min.html#plotting  
"""
import pandas as pd
import numpy as np
ts = pd.Series(np.random.randn(1000),
               index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()
pilot = ts.plot()
print(pilot)
