import pandas as pd
dataset = pd.read_csv('data.csv')
emptycells = dataset.dropna()
print(emptycells.to_string())

# removing empty cells
