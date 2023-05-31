import numpy as np
import pandas as pd

df = pd.read_csv('https://query.data.world/s/vBDCsoHCytUSLKkLvq851k2b8JOCkF')
df_1 = df.pivot_table(index = ['month','day'], 
                      values = ['rain','wind'], 
                      aggfunc = 'mean')  
print(df_1.head(20))