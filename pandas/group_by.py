import pandas as pd
import read_documents.main as m
csv=m.df_csv
#Se agrupa por valor y se le pueden dar diversas
#Opciones como "Count" para contar los elementos
print(csv.groupby('Author').count())
#Media por grupo
print(csv.groupby('Author').median())
#Minimo por grupo
print(csv.groupby('Author').min())
#Maximo por grupo
print(csv.groupby('Author').max())
#Suma entre los elementos de el grupo
print(csv.groupby('Author').sum())


#Selecciónar un indice de el grupo
print(csv.groupby('Author').count().loc['William Davis'])

#Quitar los autores como indices
print(csv.groupby('Author').count().reset_index)

#Generar por multiples factores
print(csv.groupby('Author').agg(['min','max']))

#Filtrar de una manera mas inteligente con diccionario
print(csv.groupby('Author').head(2).agg({'Reviews':['min','max'],
                    'User Rating':'sum'}))

#Llave compuesta:
print(csv.groupby(['Author','Year']).count())