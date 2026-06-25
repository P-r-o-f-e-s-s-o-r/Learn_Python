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

#MATH FUNCTIONS

array = np.array([1, 2, 3])
total = np.sum(array) 
print(total)


mean_value = np.mean(array)  
print(mean_value)


max_val = np.max(array) 
min_val = np.min(array) 
print(max_val)
print(min_val)


sqrt_array = np.sqrt(array)
print(sqrt_array)

#SLICING
import numpy as np
subset = array[1:3]  
print(subset)

#SEARCH AND SORT
import numpy as np
sorted_array = np.sort(np.array([3, 1, 2]))
print(sorted_array)

import numpy as np
indices = np.argsort(np.array([3, 1, 2]))
print(indices)

import numpy as np
array = np.array([1, 2, 3, 4])
indices = np.where(array > 2)  
print(indices)













