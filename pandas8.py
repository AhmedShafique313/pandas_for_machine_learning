import pandas as pd
dataset = {
    'calc': [5,8,6],
    'vit': [10, 6, 8]
}

var = pd.DataFrame(dataset, index= ['day1','day2','day3'])
print(var)

# printing row
print(var.loc['day2'])

