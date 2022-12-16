import numpy as np

arr=np.random.randint(1,10,(3,2))
print(arr)
print(arr.shape)
np.reshape(arr,(1,6))
print(arr)
print(arr.shape)