print("="*10,"PATTERN A","="*10)

#INPUT:
for i in range (1,5+1):
    for j in range (1,5+1):
        print("*",end="")
    print(" ")

#OUTPUT:
'''
***** 
***** 
***** 
***** 
***** 
'''
print("="*10,"PATTERN A.1","="*10)

#INPUT:
for i in range (1,5+1):
    for j in range (1,5+1):
        print(i,end="")
    print(" ")

#OUTPUT:
'''
11111
22222
33333
44444
55555
'''
print("="*10,"PATTERN A.2","="*10)

#INPUT:
for i in range (1,5+1): # type: ignore
    for j in range (1,5+1):
        print(j,end="")
    print(" ")

#OUTPUT:
'''
12345
12345
12345
12345
12345
'''
print("="*10,"PATTERN B","="*10)

#INPUT:
for i in range(1,5+1):
    for j in range(1,i+1):
        print("*",end="")
    print(" ")

#OUTPUT:
'''
*
**
***
****
*****
'''
print("="*10,"PATTERN B.1","="*10)

#INPUT:
for i in range(1,5+1):
    for j in range(1,i+1):
        print(i,end="")
    print(" ")

#OUTPUT:
'''
1
22
333
4444
55555
'''

print("="*10,"PATTERN B.2","="*10)

#INPUT:
for i in range(1,5+1):
    for j in range(1,i+1):
        print(j,end="")
    print(" ")

#OUTPUT:
'''
1
12
123
1234
12345
'''
print("="*10,"PATTERN B.3","="*10)

#INPUT:
for i in range(1, 5+1):
    for j in range(1, i+1):
        if ((i+j)%2==0):
            print("1",end="")
        else:
            print("0",end="")
    print()

#OUTPUT:
'''
1
01
101
0101
10101
'''
print("="*10,"PATTERN B.4","="*10)

#INPUT:
for i in range(1,5+1):
    for j in range(1,i+1):
        print(1,end="")
    print(" ")

#OUTPUT:
'''
1
11
111
1111
11111
'''

print("="*10,"PATTERN C","="*10)

#INPUT:
for i in range(1,6):
    for j in range(6,i,-1):
        print("*",end="")
    print(" ")

#OUTPUT:
'''
*****
****
***
**
*
'''
print("="*10,"PATTERN D","="*10)

#INPUT:
for i in range(1,10):
    if(i>5):
        for j in range(1,10-i+1):
            print("*",end="")
        print()
    else:
        for j in range(1,i+1):
            print("*",end="")
        print()
#OUTPUT:
'''
*
**
***
****
*****
****
***
**
*
'''
print("="*10,"PATTERN E","="*10)
#INPUT:

for i in range(1,6):
    print(" "*(5-i),end="")
    for j in range(1,i+1):
        print("*",end="")
    print()

#OUTPUT:
'''
    *
   **
  ***
 ****
*****
'''
print("="*10,"PATTERN E.1","="*10)
#INPUT:

for i in range (1,6):
    print(" "*(i-1),end="")
    for j in range (1,6-i+1):
        print("*",end="")
    print()

#OUTPUT:
'''
*****
 ****
  ***
   **
    *
'''

print("="*10,"PATTERN F","="*10)
#INPUT:

for i in range (1,6):
    print(" "*(5-i),end="")
    print("*"*((2*i)-1))

#OUTPUT:
'''
    *
   ***
  *****
 *******
*********
'''

print("="*10,"PATTERN F.1","="*10)
#INPUT:

for i in range (1,6):
    if (i<4):
        print(" "*(3-i),end="")
        print("*"*((2*i)-1))
    if (i>=4):
        print(" "*(i-3),end="")
        print("*"*((2*(6-i)-1)))

#OUTPUT:
'''
    *
   ***
  *****
   ***
    *
'''