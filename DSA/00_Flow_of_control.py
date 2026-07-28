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

'''print("="*10)'''

# 277 9.2 (Find the Largest Number)
'''x = float(input("Enter The Number 1 : "))
y = float(input("Enter The Number 2 : "))
z = float(input("Enter The Number 3 : "))

max = x
if y>max:
    max = y 
if z>max:
    max = z
print(max,"it is the Largest Number")'''

#292 Sum of Natural Numbers
'''
sum = 0
for n in range(1,7+1):
    sum+=n
    print("Sum of Natural Numbers of",n,"is = ",sum)
'''

#295 Factorial 
'''num = int(input("Enter The Number: ")) 
fact = 1
for n in range(num,1,-1):
    fact=fact*n
print("The Factorial of",num,"is =",fact)'''

# Number Guessing Game
'''
import random
num = random.randint(10,50)

while True:
    print("="*6,"GUESSING GAME","="*6)
    for times in range (1,6):
        Num = int(input("Enter Your Choice :"))
        if (Num == num):
            print("="*6,"You Won :)","="*6)
            break
        if (times == 5 and Num!=num ):
            print("="*6,"You LOST :(","="*6)
    cho = input("Do you Want To continue? (Y/N): ")
    if cho.lower() == "n":
        print("="*6,"GAME OVER","="*6)
        print("ANSWER: ",num)
        break
'''
# PRIME NUMBER GUESS
'''num = int(input("Enter a number: "))

if num <= 1:
    print("Not Prime")
else:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
'''

#318 problem 28                                                      Decent problems Found
'''x = int(input("Enter The Number : "))
n = int(input("Enter The Value of n : "))
sum = 0

for i in range(0,n+1):
    sum += x ** i
print("The Sum of the series is : ",sum)'''


#Fibonnaci Series
'''
t = int(input("Enter The No of Terms: "))
first = 0
second = 1
if (t<=2):
    print(first,",",second)
elif (t>2):
    print(first,",",second,end=",")
    for a in range (2,t):  # Doubt
        next = first + second
        print(next,end=",")
        first = second
        second = next
else:
    print("Enter a Valid Term")
'''

# Sum of the Digits Entered by the user
'''num = int(input("Enter The Number: "))
temp = num
sum = 0

while (num != 0):
    digit = num % 10
    sum += digit
    num = num // 10

print("The Sum of", temp, "is", sum)'''


