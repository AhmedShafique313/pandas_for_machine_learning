import pandas as pd

dataset = {
    'cars': ['Lamborgini', 'ferrari', 'lotus', 'BMW', 'Audi', 'Nissan'],
    'availability': [3,5,2,8,6,10]
}

showroom = pd.DataFrame(dataset)
print(showroom)