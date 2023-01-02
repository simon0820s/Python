import numpy as np
def f():
    x=np.linspace(1,256,num=1000)
    f=lambda x:np.log2(x)
    y=f(x)
    print(y[:11])
    return x,y