import pandas as pd
df_json=pd.read_json(
    'pandas/read_documents/d2.json')

df_csv=pd.read_csv(
    'pandas/read_documents/d1.csv',
    sep=',',
    header=0)
