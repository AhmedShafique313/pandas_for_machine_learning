import pandas as pd

df = pd.read_csv('data.csv')
df['Duration'] = pd.to_datetime(df['Duration'])
print(df.to_string())

# wrong data
df.dropna(subset=['Duration'], inplace=True)
print(df.to_string())