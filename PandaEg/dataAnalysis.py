# Importing the pandas package
import pandas as pd

# Reading the movies file
movies = pd.read_csv('https://media-doselect.s3.amazonaws.com/generic/1M2ZzY2M9PEBPJovgoaBgZdbM/movie_data.csv')

group = movies.pivot_table(values = ['actor_1_facebook_likes', 'actor_2_facebook_likes', 'actor_3_facebook_likes'],
                           index = ['actor_1_name', 'actor_2_name', 'actor_3_name'], aggfunc='sum')
                           
# Create a new column 'Total likes' which will contain the sum of likes of all three actors 
group['Total likes'] = group['actor_1_facebook_likes'] + group['actor_2_facebook_likes'] + group['actor_3_facebook_likes']

# Sort the dataframe using the 'Total likes' column
group.sort_values(by=['Total likes'], inplace=True, ascending = False)

group.reset_index(inplace=True)

j = 0

# Run a loop through the length of the column 'Total likes'
for i in group['Total likes']:
 
    temp = sorted([group.loc[j,'actor_1_facebook_likes'], group.loc[j,'actor_2_facebook_likes'], group.loc[j,'actor_3_facebook_likes']])

    if temp[0] >= temp[1]/2 and temp[0] >= temp[2]/2 and temp[1] >= temp[2]/2:
        print(sorted([group.loc[j, 'actor_1_name'], group.loc[j, 'actor_2_name'], group.loc[j, 'actor_3_name']]))
        break
    j += 1


