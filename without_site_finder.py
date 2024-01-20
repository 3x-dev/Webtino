import pandas as pd

# Load the CSV file
df = pd.read_csv('yellowpages.csv')  # Replace with your file path

# Filter rows where 'track-visit-website href' column is blank
filtered_df = df[df['track-visit-website href'].isna() | (df['track-visit-website href'] == '')]

# Save the filtered rows to a new CSV file
filtered_df.to_csv('output.csv', index=False)  # Replace with your desired output path