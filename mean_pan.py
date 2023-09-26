import pandas as pd
df = pd.read_csv('data.csv')

# for mean of column
x = df['Pulse'].mean()
y= df['Pulse'].median()
z= df['Pulse'].mode()[0]

print(x)
print(y)
print(z)