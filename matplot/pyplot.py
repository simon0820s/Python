import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(0,5,10)
y=x**2

print("X:")
print(x)
print("Y:")
print(y)
#se muestra la grafica en la que se aplican los 2 ejes
#se le puede añadir como tercer parametro un color
#tambien se le pueden añadir parametros para 
#mostrar de una manera diferente la grafica
plt.bar(x,y)
plt.show()
