'''x = int(input("Enter The Number x:"))
y = int(input("Enter The Number y:"))

Add = x+y
sub = x-y
mul = x*y
div = x/y
mod = x%y

print("Numebrs are : " , x,y)
print("ADD : ",Add)
print("SUB : ",sub)
print("MUL : ",mul)
print("DIV : ",div)
print("MOD : ",mod)

'''

'''
import random

num1=random.randint(450,950)-450
num2=random.randint(450,950)-450
avg = (num1+num2)/2
print("The Random Numbers: ",num1," ",num2)
print("The Average is : ",avg)
'''

#QUESTIONS BASED ON THE RANDOM
#PG 270 CLASS XI

#13)
'''import random
import statistics
from statistics import mean,median,mode
arr=[]

for a in range(0,5):
    num=random.randint(0,10)
    arr.append(num)
meaan=statistics.mean(arr)
medan=statistics.median(arr)
moan=statistics.mode(arr)

print("The Numbers are : ",arr)
print("The Mean of The sequence is : ",meaan)
print("The Mean of The sequence is : ",medan)
print("The Mean of The sequence is : ",moan)'''

#14
'''import random

for a in range(1,4):
    num = random.randint(100,999)
    print("Generated number:", num)  # Added for checking
    if (num % 5 == 0):
        print("The number is divisible by 5:", num)
    else:
        print("Invalid input")
        break
'''

#20

'''import math
r=8
h=15
vol = math.pi*math.pow(r,2)*h

print("The Radius of Cylinder : ",r)
print("The height of Cylinder : ",h)
print("The Volume of Cylinder : ",vol)'''