import numpy as np
arr=np.linspace(1,10,10, dtype='int8')
print(arr[(arr>5)&(arr<8)])