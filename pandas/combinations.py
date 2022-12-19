import pandas as pd
import numpy as np
import read_documents.main as m
df1=pd.DataFrame({
    'A':['A0','A1','A2','A3'],
    'B':['B0','B1','B2','B3'],
    'C':['C0','C1','C2','C3'],
    'D':['D0','D1','D2','D3']
})

df2=pd.DataFrame({
    'A':['A4','A5','A6','A7'],
    'B':['B4','B5','B6','B7'],
    'C':['C4','C5','C6','C7'],
    'D':['D4','D5','D6','D7']
})
#Concat Se puede ignorar el indice para casos especificos
print(pd.concat([df1,df2],ignore_index=True))
#Tambien se puede cambiar la dirección de crecimiento
print(pd.concat([df1,df2],axis=1,ignore_index=True))
print('')
#Merge
izq=pd.DataFrame({
    'key_left':['k0','k1','k2','k3'],
    'A':['A0','A1','A2','A3'],
    'B':['B0','B1','B2','B3'],
})
der=pd.DataFrame({
    'key_right':['k0','k1','k2','k3'],
    'C':['C0','C1','C2','C3'],
    'D':['D0','D1','D2','D3'],
})
#para usarse se debe de especificar por que llave se quiere
#hacer el merge y si son diferentes especificar por lado
print(izq.merge(der,left_on='key_left',right_on='key_right'))

