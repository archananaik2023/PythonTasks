import pandas as pd 

# Reading the movies dataframe
movies = pd.read_csv('https://media-doselect.s3.amazonaws.com/generic/1M2ZzY2M9PEBPJovgoaBgZdbM/movie_data.csv')



mv = {'aspect_ratio_mv':len(movies[movies['aspect_ratio'].isna()]), 'facenumber_in_poster_mv':len(movies[movies['facenumber_in_poster'].isna()]) }
median = {'aspect_ratio_median':movies['aspect_ratio'].median() , 'facenumber_in_poster_median':movies['facenumber_in_poster'].median() }
final = {'aspect_ratio_final':movies["aspect_ratio"].fillna(2.35).isna().sum() , 'facenumber_in_poster_final':movies["facenumber_in_poster"].fillna(1.0).isna().sum() }


# Printing the values in the three dictionaries.
print(sorted(mv.values()))
print(sorted(median.values()))
print(sorted(final.values()))