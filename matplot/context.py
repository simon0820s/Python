import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(0,10,5)
y=np.sin(x)

fig,(ax1,ax2)=plt.subplots(1,2,figsize=(5,5))
#AX1
ax1.plot(x,y,label='$sin(x)$')
ax1.legend()
ax1.set_title('Relacion X-Y')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')

#AX2
ax2.plot(y,x,label="$sin(y)$")
ax2.legend()
ax2.set_title('Relacion Y-X')
ax2.set_xlabel('Y')
ax2.set_ylabel('X')

#SHOW
plt.show()
