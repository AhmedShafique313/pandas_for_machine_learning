import pandas as pd
dataset = pd.read_csv('data.csv')
print(dataset.to_string())
# replacing values
dataset.loc[7, 'Duration'] = 50
print(dataset.to_string())