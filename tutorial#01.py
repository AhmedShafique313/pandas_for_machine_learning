# pip install jupyterlab
# pip install pandas

import pandas
dataset = {
    'cars': ['Lamborgini', 'ferrari', 'lotus', 'BMW', 'Audi', 'Nissan'],
    'availability': [3,5,2,8,6,10]
}

myvar = pandas.DataFrame(dataset)
print('   Supercars Showroom')
print('\n ')
print(myvar)