import numpy as np

arr=np.random.randint(1,20,10)
matriz = arr.reshape(2,5)
print(matriz)
#Mayor numero
print(matriz.max())  
#numeros altos bajos y mediana
np.percentile(100,arr)#50 es la mediana y 0 el minimo
np.median(matriz,1)#El segundo es el eje
np.std(arr) #desviacion estandar
np.mean(arr)#Media