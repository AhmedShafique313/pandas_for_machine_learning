import pandas as pd
dataset = pd.read_csv('data.csv')
dataset.dropna(inplace= True)
print(dataset.to_string())

# removing empty or null rows

# for filling empty cells use filna
