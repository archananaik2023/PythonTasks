# Import the Pandas package
import pandas as pd 

# Reading the input dataframe
pima = pd.read_csv('https://media-doselect.s3.amazonaws.com/generic/pLZK3n22ezVwAG2XOYW5qEx7V/pima_indian_diabetes.csv')



pima['BMI'] = round(pima['BMI'])

pima_g = pima.pivot_table(values = ['Diabetes'], index = 'BMI', aggfunc = 'sum')

pima_g.sort_values(by = 'Diabetes', inplace = True, ascending = False)

# Since BMI is present in the index of the grouped dataframe, just return the first
# index
print(int(pima_g.index[0]))