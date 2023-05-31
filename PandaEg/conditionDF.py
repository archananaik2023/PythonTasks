import pandas as pd


df = pd.read_csv('https://query.data.world/s/vBDCsoHCytUSLKkLvq851k2b8JOCkF')
df_2 = df[(df['area']> 0) & (df['wind'] >1) & (df['temp'] >15)] #Type your code here.
print(df_2.head(20))