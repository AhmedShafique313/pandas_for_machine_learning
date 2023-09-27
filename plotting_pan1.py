import pandas as pd
import matplotlib.pyplot as plt
dataset = pd.read_csv('data.csv')
dataset.plot()
plt.show()