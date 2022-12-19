import numpy as np
import pandas as pd
import read_documents.main as m
csv=m.df_csv

#Apply sirve para aplicar cualquier tipo de funcion
#a un elemento de pandas
print(csv['User Rating'])
print(csv['User Rating'].apply(lambda x:x*2))