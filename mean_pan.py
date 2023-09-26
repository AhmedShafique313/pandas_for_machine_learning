import pandas as pd
df = pd.read_csv('data.csv')

# for mean of column
x = df['Pulse'].mean()
y= df['Pulse'].median()

print(x)
print(y)