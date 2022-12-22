import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,5,10)
y=x**2

fig=plt.figure()
axes=fig.add_axes([0.1,0.1,0.8,1])
axes2=fig.add_axes([0.18,0.55,0.4,0.3])
axes.plot(x,y,'b')
axes2.plot(y,x,'r')
axes2.set_facecolor('gray')
plt.show()