import pandas as pd
import read_documents.main as m
csv=m.df_csv
fiction_csv=csv['Genre']=='Fiction'
#BORRANDO LA CULUMNA Y FILTRANDO SOLO LOS DE FICCION
print('Ficción')
print(csv.drop('Genre',axis=1)[fiction_csv])