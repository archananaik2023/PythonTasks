import pandas as pd

# Read the input series
series = pd.Series([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Read the value 'n'
n = 6

# Create a subset of the series
subset = series[series > n]

# Print the subset
print(subset)
