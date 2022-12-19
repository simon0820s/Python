import pandas as pd
#Join busca la relación entre los indices
#no sobre las columnas especificas
izq=pd.DataFrame({
    'A':['A0','A1','A2','A3'],
    'B':['B0','B1','B2','B3'],
})
izq.index=['k0','k1','k2','k3']
der=pd.DataFrame({
    'C':['C0','C1','C2','C3'],
    'D':['D0','D1','D2','D3'],
})
der.index=['k0','k2','k3','k4']
print(izq)
print(der)
print('')
print("JOIN")
#Solo cuando se hace match por indice
#Tambien se puede jugar con los datos que se entreguen
#con how
print(izq.join(der,how='outer'))#tambien recive left,right