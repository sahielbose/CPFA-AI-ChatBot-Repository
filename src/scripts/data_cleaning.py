import numpy as np
import pandas as pd

# Cleaning Cybersecurity  dataset
df = pd.read_csv('data/raw/cyber_data.csv')

for index, row in df.iterrows():
    ans_col = row['Answer']
    ans = row[ans_col]
    df.at[index, 'Answer'] = ans

df.drop(['A', 'B', 'C', 'D'], axis=1,inplace=True)

df.to_csv('data/processed/cyber_data.csv', index=False)