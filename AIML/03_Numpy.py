import numpy as np 

#ARRAY FUNCTIONS 

reshaped = np.reshape(np.arange(6), (2, 3)) #RESHAPE
print(reshaped)

flattened = reshaped.flatten() #CONVERT ANY DIM TO 1D
print(flattened)

transposed = reshaped.T #TRANSPOSE
print(transposed)

a = np.array([1, 2])
b = np.array([3, 4])
concatenated = np.reshape(np.concatenate((a, b)),(2,2))
print(concatenated)