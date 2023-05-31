# Importing the pandas package
import pandas as pd 

# Reading the dataframe
movies = pd.read_csv('https://media-doselect.s3.amazonaws.com/generic/1M2ZzY2M9PEBPJovgoaBgZdbM/movie_data.csv')

# Print out the indices of the rows in which both these columns have missing values
# as a list
null_rows = list(movies[(movies['actor_1_facebook_likes'].isnull()) & (movies['actor_1_facebook_likes'].isnull()) ].index)

print(null_rows)

# Write your code for dropping these particular rows here

movies_final = movies.drop(null_rows, axis=0)
# Print the number of remaining rows
print(movies_final.shape[0])