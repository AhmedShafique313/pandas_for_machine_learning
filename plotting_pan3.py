import pandas as pd
import matplotlib.pyplot as plt
dataset = pd.read_csv('data.csv')
dataset['Duration'].plot(kind='hist')
plt.show()