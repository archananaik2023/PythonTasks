import numpy as np
import pandas as pd

df1 = pd.read_csv("nba.csv")
  
# Creating second dataframe
df2 = pd.read_csv("nba1.csv")
  
# Creating third dataframe
df3 = pd.read_csv("nba1.csv")
  
# Concatenating the dataframes

concatenated_df = pd.concat([df1, df2, df3], ignore_index=True)
concatenated_df.index = concatenated_df.index + 1
print(concatenated_df)
