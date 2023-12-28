import pandas as pd

df = pd.read_csv('Games Sales_Case Study.csv')

# Oldest and newest games
df['Release'] = pd.to_datetime(df['Release'])
oldest = df.loc[df['Release'].idxmin(), 'Name']
newest = df.loc[df['Release'].idxmax(), 'Name']
print(f"Oldest Game: {oldest}") 
print(f"Newest Game: {newest}")

# Publisher with most games
publisher_counts = df['Publisher'].value_counts()
top_publisher = publisher_counts.index[0]
print(f"\nTop Publisher: {top_publisher}")

# Developer with most games
developer_counts = df['Developer'].value_counts()
top_developer = developer_counts.index[0]
print(f"\nTop Developer: {top_developer}")

# Top selling series
sales_by_series = df.groupby('Series')['Sales'].sum().reset_index()
top_series = sales_by_series.sort_values('Sales', ascending=False).iloc[0]['Series']
print(f"\nTop Selling Series: {top_series}")

# Series with most game entries
series_counts = df['Series'].value_counts().reset_index()
series_counts.columns = ['Series', 'Count'] 
series_with_most = series_counts.sort_values('Count', ascending=False).iloc[0]['Series']

print(f"\nMost Games in a Series: {series_with_most}")