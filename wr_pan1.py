import pandas as pd
# deleting rows where Duration is higher than 120
df = pd.read_csv('data.csv')
for i in df.index:
    if df.loc[i, 'Duration'] > 120:
        df.drop(i, inplace= True)

print(df.to_string())