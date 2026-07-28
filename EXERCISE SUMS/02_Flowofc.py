#PG 277

'''a=int(input("Enter the Number a: "))
b=int(input("Enter the Number b: "))
c=int(input("Enter the Number c: "))
sum1=0
sum2=0
sum1 = a+b+c

if (a!=b and a!=c):
    sum2+=sum1
if (b!=a and b!=c):
    sum2+=sum1
if (c!=a and c!=b):
    sum2+=sum1

print ("Sum of Numbers : ",sum1)
print ("Sum of non Numbers : ",sum2)
'''

#292
'''sum = 0
for i in range(1,8):
    sum+=i
    print("The sum of Numbers 1 to ",i," is : => ",sum)
print("The sum of Numbers 1 to 7 is : ",sum)'''

#295

'''num = int(input("Enter The Number For Factorial: "))
fact =1
a = 1

while (a<=num):
    fact*=a
    a+=1
print("The Factorial of The Number",num,"is :",fact)
'''
#297
'''import random

print("*"*5," GUESSING THE NUMBER ","*"*5)
print("\n")
rnum=random.randint(1,50)

for i in range (1,6):
    print("      YOUR",i,"CHANCE      ")
    unum=int(input("Enter The Number 1 to 50: "))
    if (unum==rnum):
        print("-"*5," YOU WON ","-"*5)
        break
    else:
        print("-"*5," YOU LOSE ","-"*5)

print("\n")
print("-"*5," GAME OVER ","-"*5)'''

#300
'''for a in range(1,11):
    print(a)
    if(a%2==0):
        print(a)
        break
print("\n")

for b in range(1,11):
    print(a)
    if(a%2==0):
        continue
'''
# 303 
'''num = int(input("Enter the Number : "))

if num > 1:
    for a in range(2, int(num**0.5) + 1):
        if num % a == 0:
            print(num, "is Not Prime")
            break
    else:
        print(num, "is Prime")
else:
    print("Enter a number greater than 1")'''