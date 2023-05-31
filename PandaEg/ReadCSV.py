import pandas as pd
import numpy as np
  
# making data frame from csv file
df = pd.read_csv("nba.csv")
print(df)


# Sort the DataFrame by Date of Joining in ascending order
df_sorted_by_date = df.sort_values('Date of Joining')

# Sort the DataFrame by Salary in descending order
df_sorted_by_salary = df.sort_values('Salary', ascending=False)

# Calculate the average salary
average_salary = df['Salary'].mean()

# Calculate the maximum age
max_age = df['Age'].max()

# Calculate the total salary
total_salary = df['Salary'].sum()

# Display the sorted DataFrame
print("Sorted by Date of Joining:")
print(df_sorted_by_date)

print("\nSorted by Salary:")
print(df_sorted_by_salary)

# Display the aggregate functions
print("\nAverage Salary:", average_salary)
print("Maximum Age:", max_age)
print("Total Salary:", total_salary)


# Declare a list that is to be converted into a column
address = ['Delhi', 'Bangalore', 'Chennai', 'Patna','Mumbai','Pune','Bangkok','Yemen','Lucknow','New Jersey','Dallas']
  
# Using 'Address' as the column name
# and equating it to the list
df['Address'] = address

# Check newly added column

print(df)