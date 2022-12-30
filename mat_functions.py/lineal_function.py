import numpy as np
import matplotlib.pyplot as plt
n=100
m=10
b=5
def f(x):
    return m*x+b

x=np.linspace(-10,10,num=n)

y=f(x)

fig,ax=plt.subplots()
ax.plot(x,y)
ax.grid()
plt.show()