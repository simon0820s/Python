import pandas as pd
import read_documents.main as m
csv=m.df_csv
#Informacion de la tabla
print(csv.info())
#Describe información estadistica de la tabla
print(csv.describe())
#HEAD solo entrega una determinada cantidad de filas
print(csv.head(2))#2 primeras filas
#Ver cuanta memoria esta usando mi frame
print(csv.memory_usage(deep=True))
#Entrega las repeticiones de el uso de cada autor
print(csv['Author'].value_counts())
#Eliminar valores duplicados
csv.drop_duplicates()
#Ordenar valores || de manera ascendente o descendente
print(csv.sort_values('Year',ascending=True))