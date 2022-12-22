import matplotlib.pyplot as plt
import numpy as np
#Definir el arreglo
x=np.linspace(0,5,10)
#Definir el estilo
plt.style.use('dark_background')
fig,ax=plt.subplots(figsize=(8,8))
#Atributos de estilo

#se puede colorear con rgb
ax.plot(x,x+4,color='#F37F66')
#Se pueden poner atributos de transparencia con alpha
ax.plot(x,x+1,color='green',alpha=0.8)
#Se puede modificar el grosor de la linea
ax.plot(x,x+2,color='blue',linewidth=8)
#Se puede modificar el estilo de la linea
ax.plot(x,x+3,color='orange',linestyle='--')
#Se pueden poner marcadores, su tamaño y color
ax.plot(x,x+4,color='orange',marker='v',markersize=8,markerfacecolor='green')

#SHOW
plt.show()