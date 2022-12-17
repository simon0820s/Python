import pandas as pd
import numpy as np
import read_documents.main as m

csv=m.df_csv.copy()
print("CSV COMPLETO:")
print(m.df_csv)
print('')
del csv['Price']
del csv['Genre']
del csv['Reviews']
del csv['User Rating']
print("CSV SIN DATOS DE COMPRA:")
print(csv)
print('')
print("CSV ORIGINAL SIN AFECTARSE:")
print(m.df_csv)
print('')
#Nueva Columna:
print("NUEVA COLUMNA")
csv['New Column']=np.nan
print(csv)
