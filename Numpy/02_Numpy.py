import numpy as np
'''
#ARITHEMETIC
arr = np.array([25,26,5,2])
print(arr+1)
print(arr-1)
print(arr*2)
print(arr ** 3)
print(arr/5)

brr = np.array([5,2,3,10])
print(arr+brr)
print(arr-brr)
print(arr*brr)
print(arr ** brr)
print(arr/brr)

age = np.array([25,24,53,17,18,6])
print(age<18)
print(age == 18)
print(age>=18)
age[age<18] = 18 #CHANGE THE AGE OF PPL WHO ARE <18 TO 18
print(age)'''

'''
#BROADCAST & LISTING

arr =np.array([[1,2,3],
               [4,5,6],
               [7,8,9]])
brr = np.array([1,2,3])
k = list(arr*brr)
print(k[1][0])
'''

#Functions 
'''
arr = np.zeros(5)
print(arr)
arr = np.zeros((2,3))
print(arr)
arr = np.zeros((2,4,3))
print(arr)

arr = np.ones(5)
print(arr)

arr = np.full(2,3)
print(arr)
arr = np.full((2,3),3)
print(arr)
arr = np.full((2,3,2),3)
print(arr)
'''

#IDENTITY MATRIX
'''
arr = np.eye(3)
print(arr)
'''
'''
arr = np.arange(0,100,15) # start,stop,step
print(arr)
arr = np.linspace(0,100,6)
print(arr)
arr = np.linspace(0,100,5) # start,stop,Count(no of)
print(arr)
arr = np.sum(arr)
print(arr)
arr = np.min(arr)
print(arr)
arr = np.max(arr)
print(arr)
arr = np.std(arr)
print(arr)
arr = np.var(arr)
print(arr)
arr = np.argmin(arr) # Prints Which Index has Min Number 
print(arr)
arr = np.argmax(arr) # Prints Which Index has Max Number 
print(arr)

brr =np.array([[1,2,3],
               [4,5,6]])
print(np.sum(brr))
print(np.sum(brr,axis=1))
'''
'''
marks = np.array([50,100,65,45,76])
print(marks)
print(marks[marks>50]) #Tells the value
print(marks>50) #Tells the Boolean Value

#Filtered Array
pass_mark = marks[marks>50]
print(pass_mark)

even = marks[(marks>=50) | (marks%2==0)]
print(even)

arr = np.array([[1,2,3],
                [4,5,6]])

even = np.where(arr%2==0, arr, 0) #Except Even Number all places is filled with Zero . OUTPUT will be of Same Dimentsons
print(even)

'''