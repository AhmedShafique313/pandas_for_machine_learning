import pandas as pd
dataset = pd.read_csv('data.csv')
# print(dataset.head(16))
print(dataset.head())
print(dataset.tail())

# getting info about the data
print(dataset.info())