import numpy as np
def f(x):
    f1=lambda x:x**2
    f2=lambda x:np.sin(x)

    y=f2(f1(x))
    return y