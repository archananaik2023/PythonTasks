import pandas as pd
import numpy as np


left = pd.read_csv("nba.csv")
  
right = pd.read_csv("nba1.csv")
                        
df = left.join(right.set_index("Name"), on="Name", lsuffix='_left', rsuffix='_right')


print("Joined df:\n", df)