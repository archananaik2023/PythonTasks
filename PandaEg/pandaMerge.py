import numpy as np
import pandas as pd

left = df1 = pd.read_csv("nba.csv")
  
right = df1 = pd.read_csv("nba1.csv")
                        
# Merging the dataframes                      
mergePD = pd.merge(left, right, how ='inner', on ='Name')
  
# Merging the dataframes

print("Merged dataframes : ", mergePD)