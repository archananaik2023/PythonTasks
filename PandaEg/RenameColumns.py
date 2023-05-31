# Importing the pandas package
import pandas as pd

# Reading the dataframe
df = pd.read_csv('https://media-doselect.s3.amazonaws.com/generic/XWvQjYY4LZWdxLvPWOj2pPwn/heart.csv')


df_columns = df.columns.map(lambda x : x.capitalize())

# Printing the final columns. 
print(df_columns)