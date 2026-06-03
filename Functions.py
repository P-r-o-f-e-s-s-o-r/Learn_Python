'''
#PROGRAME TO ADD NUMBERS 

def sum(x,y):
    s = x+y
    return s
num1 = int(input("Enter the Number 1 : "))
num2 = int(input("Enter the Number 2 : "))
k = sum(num1,num2)
print("The Sum of",num1,"and",num2,"is : ",k)
'''

'''
#pg without arg and return
def add():
    a=int(input("Enter the value of a:"))
    b=int(input("Enter the value of b:"))
    c=a+b
    print("the sum of numbers is:",c)
add()

#pg with arg and without return

def sum(x,y):
    print("the sum of two values are:",x+y)
m=int(input("Enter the value of m:"))
u=int(input("Enter the value of u:"))
sum(m,u)

#pg with arg and with return

def calc(k,e):
    j=k+e
    return j
k=int(input("Enter the value of k:"))
e=int(input("Enter the value of e:"))
s=calc(k,e)
print("the sum of two numbers is:",s)

#pg without arg and with return

def calsu():
    i=int(input("Enter the value of i:"))
    h=int(input("Enter the value of h:"))
    o=i+h
    return o
print("the sum of two numbers is :",calsu())

'''
'''
from math import pi                                       #built in scope

#x=1                                                      #global scope
def outer():
    #x=2                                                  #enclosing scope
    def inner():
        #x=3                                              #local scope
        print("the inner value of the function is:",pi)
        return
    inner()
    print("the outer value of x is:",pi)
    return
outer()
print("the global value of pg is:",pi)

'''


'''
x=1                                                      #global
def outer():
    global x
    x=2                                                  #enclosing
    def inner():
        x=3                                              #local 
        print("the inner value of the function is:",x)
        return
    inner()
    print("the outer value of x is:",x)
    return
outer()
print("the global value of pg is:",x)

# using non local func
'''
'''
y=4                                                      #global
def outter():
    y=5                                                  #enclosing
    def iner():
        nonlocal y
        y=6                                              #local 1
        print("the inner value of the function is:",y)
        return
    iner()
    print("the outer value of x is:",y)
    return
outter()
print("the global value of pg is:",y)
'''
 

#VIST ONCE AGAIN
def Lshif(Arr,n):
    for i in range(len(Arr)):
        Arr[i-n] = Arr[i]
    print("The Final Matrix with ",n,"is :",Arr)

def main():
    ar = [10,20,30,40,12,11]
    num = int(input("Enter the Spacing Number : "))
    Lshif(ar,num)
main()