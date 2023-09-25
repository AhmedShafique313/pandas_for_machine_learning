import pandas as pd

dataset = pd.read_json('datajson.json')
print(dataset.to_string())

