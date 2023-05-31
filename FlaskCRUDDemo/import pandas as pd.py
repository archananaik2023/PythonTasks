import pandas as pd

# Create a sample dataframe
df = pd.DataFrame({
    'col1': [10, -20, 30, -40],
    'col2': [1.1, -2.2, 3.3, -4.4]
})

# Negate each value in column 'col1'
df['col1'] = df['col1'].abs().multiply(-1)

# Print the resulting dataframe
print(df)
