import numpy as np  #Import Numpy

'''
array = [12,4,2]
array = np.array(array) #Converting Normal list to Numpy array
'''

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

'''
#OBJ DTYPE
arra = np.array([1,2,"Launch"],dtype = np.object_)
print(arra)
print(arra.dtype)
print(arra.nbytes) #No of Elements [Result = 24 (3*8)] [no of elements * (bytes/8)]
'''
'''
#TYPE CONVERSION
print(array)
print(array.dtype)
print(array.nbytes)

array = array.astype(np.str_)  #CONVERT Int to Str
print(array)
print(array.dtype)
print(array.nbytes)'''


'''
#===========================================================
 #Prints dimention (single dot - 0D) , (Two connected Dots - 1D) , (Square - 2D) , (Cube - 3D),(Treseract - 4D)
array_1 = np.array(1)
print(array_1.ndim) #0D
array_2 = np.array([1,2,3,4,4,5])
print(array_2.ndim) #1D
array_3 = np.array([[1,2],
                  [3,4],
                  [4,3]]) #SINGLE MATRIX
print(array_3.ndim) #2D

array_4 = np.array([[[1,2,3],
                   [4,5,6]],
                   [[7,8,9],
                    [10,11,12]]])
print(array_4.ndim) #3D [Length [rows] , Breath [Columns] , Layers [Each Set of Array]]

print(array_2[2])
print(array_3[2][0])
print(array_4[1][0][2]) #chain indexing
print(array_4[1,0,2]) #Multi dimentional indexing

#SHAPES
print(array_4.shape) #(layers , rows , columns)

#RESHAPE
print(array_2.reshape(2,3)) #Change the Shape of Array
print(array_2.reshape(3,-1)) #Columns will get automaticlly saturated

#SLICING
print(array_4[1:3])
'''