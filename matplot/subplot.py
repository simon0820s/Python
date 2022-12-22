import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(0,5)
y=x**2

#Se trabajan las graficas como si fuesen una tabla
#como primer parametro filas y el segundo columnas
#el tercero es la posición de la grafica en la tabla
#Tambien se pueden trabajar 2 cosas en una sola grafica
plt.subplot(1,2,1)
plt.plot(x,y)
plt.plot(y,x)
plt.subplot(1,2,2)
plt.hist(x,y)
plt.show()