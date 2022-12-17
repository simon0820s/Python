import pandas as pd
import main as m
#Filter by row
print(m.df_csv[:4])
#Filter by Column
print(m.df_csv['Name'])
#Filter by Column and row USE LOC!!
print(m.df_csv.loc[:3,['Reviews']])
#Filter by Index
print(m.df_csv.iloc[:,0:3])