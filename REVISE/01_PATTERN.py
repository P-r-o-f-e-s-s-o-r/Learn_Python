print("="*3,"P1","="*3)

for i in range(1,6):
    for j in range(1,6):
        print("*",end="")
    print()
print("="*8)

print("="*3,"P2","="*3)

for i in range(1,6):
    for j in range(1,6):
        print(i,end="")
    print()
print("="*8)

print("="*3,"P3","="*3)

for i in range(1,6):
    for j in range(1,6):
        print(j,end="")
    print()
print("="*8)

print("="*3,"P4","="*3)

for i in range(1,6):
    for j in range(1,i+1):
        print("*",end="")
    print()
print("="*8)

print("="*3,"P1","="*3)

for i in range(1,6):
    for j in range(1,i+1):
        print(i,end="")
    print()
print("="*8)

print("="*3,"P1","="*3)

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()
print("="*8)

print("="*3,"P7","="*3)

for i in range(1,6):
    for j in range(1,i+1):
        if((j+i)%2==0):
            print("0",end="")
        else:
            print("1",end="")
    print()
print("="*8)

print("="*3,"P8","="*3)

for i in range(1,6):
    for j in range(1,i+1):
        print("1",end="")
    print()
print("="*8)

print("="*3,"P9","="*3)

for i in range(1,6):
    for j in range(6,i,-1):
        print("*",end="")
    print()
print("="*8)

print("="*3,"P10","="*3)

for i in range(1,10):
    if(i<=5):
        for j in range(1,i+1):
            print("*",end="")
        print()
    else:
        for j in range(10,i,-1):
            print("*",end="")
        print()
print("="*8)
print("="*3,"P11","="*3)

for i in range(1,6):
    print(" "*(5-i),end="")
    for j in range (1,i+1):
        print("*",end="")
    print()
print("="*8)

print("="*3,"P12","="*3)

for i in range(1,6):
    print(" "*(i-1),end="")
    for j in range (6,i,-1):
        print("*",end="")
    print()
print("="*8)

print("="*3,"P13","="*3)

for i in range(1,6):
    print(" "*(5-i) , end="")
    print("*"*((2*i)-1))
print("="*8)

print("="*3,"P14","="*3)

for i in range(1,6):
    if(i<=3):
        print(" "*(5-i) , end="")
        print("*"*((2*i)-1))
    else:
        print(" "*(i-1) , end="") #
        print("*"*((2*i)-1))
        
print("="*8)

