import pandas as pd

df = pd.read_csv('https://query.data.world/s/vBDCsoHCytUSLKkLvq851k2b8JOCkF')


by = df.groupby(by=['month','day']) 
df_1 = by[['rain', 'wind']].mean()


print(df_1.head(20))