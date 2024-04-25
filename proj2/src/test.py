# THIS FILE IS HERE FOR TESTING PURPOSES ONLY
# THE DELIVERED ONE IS THE JUPYTER NOTEBOOK

import pandas as pd

df = pd.read_csv('../data/data.csv')

print(set(df['class']))