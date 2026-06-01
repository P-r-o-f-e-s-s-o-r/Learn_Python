#INDEXING A WORD
'''
word = input("Enter the Word : ")
L = list(word)
length = len(L)
print("The List is : ",L)
for i in range(length):
    print("At the Indexes ",i,"and", i-length ," : ",L[i])
'''

'''#LIST SLICING 
L = [10,12,14,20,22,24,30,32,34]
L1 = [1,2,3]
print(L[3:-3])
print(L[3:30])
print(L[-15:7])
print(L[2:-5])
print(L[6:10])
print(L[10:20])
print(L[0:10:2])
print(L[2:10:3])
print(L[::3])
print(L[::-1])
print(L[3:-3]+L1[1:])
L1[1:] = "ABC"
print(L1)'''


'''
#CREAT 2D MATRIX
L=[]
rows = int(input("Enter the No of Rows : "))
Columns = int(input("Enter the No of Columns : "))
for i in range(rows):
    row = []
    for j in range(Columns):
        Ele = int(input("Enter the Value "+str(i)+","+str(j)+": "))
        row.append(Ele)
    L.append(row)

for k in range(len(L)):
    print(L[k])
'''
'''
#FIND THE MIN NUMBER IN THE LIST

L = [150,220,2230,1]
max = L[0]
min = 0
for i in range (len(L)):
    if (max<L[i]):
        min = max
    else:
        min = L[i]
print("The Minimum value is : ",min,"of index ",i)
'''
'''
#SEARCH AN ELEMENT IN AN GIVEN LIST
num = input("Enter the Numbers as group : ")
L = num.split()
no = input("Enter the Number wanted to search : ")
for i in range(len(L)):
    if (no == L[i]):
        print("The Element you Searched of ",no,"is on index ",i)
    else:
        print("The Element you searched is not in the Given lisSt")
'''
'''
#FREQUENCY FINDER OF NUMBERS
L = eval(input("Enter the Number : "))
num = int(input("Enter the Number : "))
print("The Number of occurance of ",num,"in list is : ",L.count(num))
'''