import pandas as pd
import numpy as np
  
# making data frame from csv file
df = pd.read_csv("IncomeData.csv")
print("Original dataframe")
print(df)


# return first few rows
print("\nHead Function")
print(df.head())


# return total number of rows in the dataset, 
# names of the columns, their data type, and any missing value

print("\nInfo Function")
print(df.info())

# return The describe method computes some summary statistics for numerical columns, 
# like mean and median. “count” is the number of non-missing values in each column.

print("\nDescribe Function")
print(df.describe())

# returns the number of rows followed by the number of columns in df.

print("\nShape Function")
print(df.shape)

# to cast a Python object to a particular datatype astype() is used for this. 
# It is a useful function in case data is not stored in the correct format

df['Income']= df['Income'].astype('int')

# sort_values - It will sort the values on the basis of Age desceding and Income Asc

print("Sorting Function")
print(df.sort_values(['Age','Income'], ascending=[False, True]).head())

# value_counts() is used when you want to see the count of unique values of various columns.
print("\nValue counts")
print(df['Income'].value_counts())

# drop_duplicates() removes duplicate rows from the dataset.
# Inplace=True implies that the changes will be made to the original dataset.

print("Drop duplicates")
print(df.drop_duplicates(inplace=True))

# Subsetting rows and columns

print("\nSubsetting rows and columns")
idata_subsetcol= df[['Name','Age','Occupation']]
print(idata_subsetcol.head())

# Adding new column

print("\nAdding new column")
df['Savings']= df['Income'] - df['Expenses']
print(df.head())

# set_index() & reset_index() 

# If you want to convert any column of a dataset as its index, it can be done via set_index

print("\nIndex")
df_index= df.set_index('Name')
print(df_index.head())

print("\nReset Index")
df_reset_index = df.reset_index()
print(df_reset_index.head())

print("\nloc ")
idata_loc=df.loc[(df.Age >= 32) & (df.Gender == 'Male')]
print(idata_loc.head())

print("\niloc")
inc_iloc=df.iloc[0:4,1:3]
print(inc_iloc.head())

print("Groupby")
income_agg = df.groupby("Age")["Income"].mean()
print(income_agg)

print("Pivot Table")
inc_pivot= df.pivot_table('Age', index='Gender', columns='Occupation')
print(inc_pivot)
