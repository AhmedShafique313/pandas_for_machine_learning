import pandas as pd
dataset = pd.read_csv('data.csv')
print(dataset.corr())