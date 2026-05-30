'''
#FIND  
num1 = int(input("Enter The Number 1: "))
num2 = int(input("Enter The Number 2: "))
num3 = int(input("Enter The Number 3: "))

Sum = num1+num2+num3
sum = 0
if (num1/num2 == 1):
    sum = num3
elif (num1/num3 == 1):
    sum = num2
elif (num2/num3 == 1):
    sum = num1
else :
    sum = Sum

print("The Sum of All Numbers : ",Sum)
print("The Sum of All Non Duplicate Numbers : ",sum)
''' 


'''
#FIND THE LARGEST NUMBER 
num1= int(input("Enter The Number 1 : "))
num2= int(input("Enter The Number 2 : "))
num3= int(input("Enter The Number 3 : "))

max = num1
if (num2>max):
    max = num2
elif (num3>max):
    max = num3
else:
    print("Error")

print("The Largest Number IS : ",max)
'''


'''
#FACTORIAL 
num = int(input("Enter The Number : "))
fact = 1
for i in range (1,num+1):
    fact=fact*i
print("The Factorial Value : ",fact)
'''

'''
n = int(input("Enter The Number : "))
odd = 0
Even = 0

for a in range(1,n+1):
    if (a%2 == 0):
        Even+=a
    if (a%2!=0):
        odd+=a
print("The Sum of Odd Numbers : ",odd)
print("The Sum of Even Numbers : ",Even)
'''


'''
#GUESS THE NUMBER GAME
import random

print("="*8,"GUESS THE NUMBER","="*8)
num = random.randrange(10,50)

for life in range(5,0,-1):
    cho = int(input("Enter the Guessed Number: "))
    print("You Have ",life,"life")
    if(cho == num ):
        print("You won")
        break
    if (life == 0):
        print("You Lose")
        break

    '''
'''
#DIFFERENCE B/W THE CONTINUE AND BREAK
for a in range(1,10):
    print(a)
    if(a%2==0):
        break
print("\n")
for b in range(1,10):
    if(b%2==0):
        continue
    else:
        print(b)
'''
#PRIME NUMBER 
'''
num = int(input("Enter Your Number"))
lim = int(num/2)+1
for i in range(2,lim):
    rem = num%i
    if (rem==0):
        print(num,"Is not a Prime Number")
    else:
        print("Its a Prime Number")
'''

#SEGREGATE NUMS 
'''
#MINE
num = int(input("Enter The Input : "))
no = len(str(num))

for i in range(1,no):
    k = num%10
    print(k)
#GPT
num = int(input("Enter The Input : "))
no = len(str(num))

for i in range(no):      # Changed to loop exactly 'no' times
    k = num % 10         # Get the last digit
    print(k)             # Print the digit
    num = num // 10      # Remove the last digit from 'num'
'''