import numpy as np 

#ARRAY FUNCTIONS 

reshaped = np.reshape(np.arange(6), (2, 3)) #RESHAPE
print(reshaped)

flattened = reshaped.flatten() #CONVERT ANY DIM TO 1D
print(flattened)

transposed = reshaped.T #TRANSPOSE
print(transposed)