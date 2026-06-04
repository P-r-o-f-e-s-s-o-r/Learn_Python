import numpy as np  #Import Numpy

array = [12,4,2]
array = np.array(array) #Converting Normal list to Numpy array
'''
print(array)
array = array*2 
print(array)

'''
'''
#DTYPE 
print(array.dtype)
arra = np.array([1,2,3],dtype = np.int8)
print(arra.dtype)
print(arra.nbytes) #No of Elements [Result = 3 (3*1)]
'''
#int8, int16, int32, int64 []
#2^8=256 >-128 --> 127 [If it exceed 127 means Error will be occur]

'''
#BYTES
print(array.dtype)
arra = np.array([1,2,3],dtype = np.int64)
print(arra.dtype)
print(arra.nbytes) #No of Elements [Result = 24 (3*8)] [no of elements * (bytes/8)]

arra = np.array([1,2,3],dtype = np.str_) #STRING
print(arra)
'''
#OBJ DTYPE
arra = np.array([1,2,"Launch"],dtype = np.object_)
print(arra)
print(arra.dtype)
print(arra.nbytes) #No of Elements [Result = 24 (3*8)] [no of elements * (bytes/8)]
