#Description
#You are provided with the dataset of a company which has offices across three cities - Mumbai, Bangalore and New Delhi. The dataset contains the rating (out of 5) of all the employees from different departments (Finance, HR, Marketing and Sales). 

#The company has come up with a new policy that any individual with a rating equal to or below 3.5 needs to attend a training. Using dataframes, load the dataset and then derive the column ‘Training’ which shows ‘Yes’ for people who require training and ‘No’ for those who do not.

import numpy as np
import pandas as pd

# Condition whose rating is less than 3.5

df = pd.read_csv('https://media-doselect.s3.amazonaws.com/generic/NMgEjwkAEGGQZBoNYGr9Ld7w0/rating.csv')

df['Training'] = df.Rating.apply(lambda x : 'Yes' if x < 3.5 else 'No')
print(df.head())