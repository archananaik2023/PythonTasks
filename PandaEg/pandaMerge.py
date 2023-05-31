import numpy as np
import pandas as pd


df_1 = pd.read_csv('https://query.data.world/s/vv3snq28bp0TJq2ggCdxGOghEQKPZo')
df_2 = pd.read_csv('https://query.data.world/s/9wVKjNT0yiRc3YbVJaiI8a6HGl2d74')
df_3 = pd.merge(df_1,df_2,how='inner', on='unique_id')
print(df_3.head(20))