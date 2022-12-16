import numpy as np
arr = np.arange(0,11)
print(arr)
arrc=arr.copy()
pedazo=arrc[0:6]
pedazo[:]=100
print(pedazo)
print(arr)