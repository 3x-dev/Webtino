import pandas as pd

# Load the CSV file
df = pd.read_csv('yellowpages.csv')

# Filter rows where 'track-visit-website href' column is blank, has a Facebook website, or has a Yelp website
filtered_df = df[df['track-visit-website href'].isna() | 
                 (df['track-visit-website href'] == '') | 
                 df['track-visit-website href'].str.contains('facebook.com', na=False) |
                 df['track-visit-website href'].str.contains('yelp.com', na=False)]

# Save the filtered rows to a new CSV file
filtered_df.to_csv('output.csv', index=False)
