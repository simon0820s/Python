import pandas as pd
#Json
df_json=pd.read_json(
    'pandas/read_documents/d2.json')
print(df_json)
print('')

#CSV
df_csv=pd.read_csv(
    'pandas/read_documents/d1.csv',
    sep=',',
    header=0)
print(df_csv)
