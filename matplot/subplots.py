import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,5,10)
y=np.linspace(0,50)

fig, axes = plt.subplots(2,3)
#Fila 1
axes[0,0].plot(x,np.cos(x))
axes[0,1].plot(x,np.sin(x),'red')
axes[0,2].plot(x,np.tan(x),'green')
#Fila 2
axes[1,0].plot(x,np.cos(x)**2,'orange')
axes[1,1].plot(x,np.sin(x)**2,'yellow')
axes[1,2].plot(x,np.tan(x)**2,'purple')
fig.tight_layout()
plt.show()