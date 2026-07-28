#BASICS
'''
Lst1 = [1,2,3,4]
Lst2 = [4,6,7,8]
Lst = Lst1 + Lst2
print(Lst)

a = input("Enter the word : ")
k = list(a)
print(k)

lst = [1,23,4,3,3,2,3,2]
print(lst[0:10:2])

l1 = [1,2,3,4]
l1[2:]="abcd"
print(l1)

l2 = [1,2,3,4]
l2[2:]="123"
print(l2)

'''
# 380

'''
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
sl1 = lst[5:15]
sl2 = lst[::4]

k1 = sum(sl1) 
print("List is :",end="")
for i in sl1:
    print(i,end=" ")
print()
print("The sum of elements in List is :",k1)

print()

k2= sum(sl2)
avg = k2/len(sl2)
print("List is :",end="")
for i in sl2:
    print(i,end=" ")
print()
print("The Avg of elements in List is :",avg)
'''
#CREATING 2D LIST
'''
lst=[]
row = int(input("Enter The No of Rows : "))
Column = int(input("Enter The No of Column : "))

for i in range(row):
    row=[]
    for j in range(Column):
        element = int(input("Enter The Element "+str(i)+","+str(j)+":"))
        row.append(element)
    lst.append(row)

for i in lst:
    print(i)
'''

# USING INSERTION , DELETION 
'''
lst = []
while True :
    print("="*10,"WELCOME TO LIST GAME","="*10)
    print(" "*11,"1. Insert")
    print(" "*11,"2. Delete")
    print(" "*11,"3. Display")
    print(" "*11,"4. Exit")
    if (len(lst)==0):
        print("Kindly Enter the Elements to start the Game")
        Num = int(input("Enter How Many Elements You wanna add?: "))
        for i in range(Num):
            element = int(input("Enter The elements: "))
            lst.append(element)
    else:
        cho = int(input("Enter The Choice : "))
        if (cho == 1):
            print("*"*11,"  INSERTION  ","*"*11)
            print(" "*11,"1.Insert By the Element")
            print(" "*11,"2.Insert By the list")
            print(" "*11,"3.Insert By the Position")
            choo = int(input("Enter the Choice Player: "))
            if (choo == 1):
                print("*"*6,"Insert By the Element","*"*6)
                while True:
                    ele = int(input("Enter the Elements : "))
                    lst.append(ele)
                    c = input("Do you Want to continue the process?(Y/N) ")
                    if (c.lower()=="n"):
                        break
            elif (choo == 2):
                print("*"*6,"Insert By the list","*"*6)
                while True:
                    ele = eval((input("Enter the list : ")))
                    lst.extend(ele)
                    c = input("Do you Want to continue the process?(Y/N) ")
                    if (c.lower()=="n"):
                        break
            elif(choo == 3):
                print("*"*6,"Insert By the position","*"*6)
                while True:
                    print("Preview the list once: ",lst)
                    po = int(input("Enter the position : "))
                    ele = int(input("Enter the Element : "))
                    lst.insert(po,ele)
                    c = input("Do you Want to continue the process?(Y/N) ")
                    if (c.lower()=="n"):
                        break
            else:
                print("Enter the Valid Option")
        elif(cho == 2):
            print(" "*11,"  DELETION  ","*"*11)
            print(" "*11,"1.Delete By the Element")
            print(" "*11,"2.Delete By the slice")
            print(" "*11,"3.Delete By the Position")
            choo = int(input("Enter the Choice Player: "))
            if (choo == 1):
                print("*"*6,"Delete By the Element","*"*6)
                while True:
                    print("Preview the list once: ",lst)
                    ele = int(input("Enter the Element : "))
                    if ele in lst:
                        lst.remove(ele)
                    else:
                        print("Value error")
                    print("After Remove the list: ",lst)
                    c = input("Do you Want to continue the process?(Y/N) ")
                    if (c.lower()=="n"):
                        break
            elif (choo == 2):
                print("*"*6,"Delete By the slice","*"*6)
                while True:
                    print("Preview the list once: ",lst)
                    s1 = int(input("Enter the Slice1 : "))
                    s2 = int(input("Enter the Slice2 : "))
                    del lst[s1:s2]
                    print("After deletion the list: ",lst)
                    c = input("Do you Want to continue the process?(Y/N) ")
                    if (c.lower()=="n"):
                        break
            elif (choo == 3):
                print("*"*6,"Delete By the Position","*"*6)
                while True:
                    print("Preview the list once: ",lst)
                    s1 = int(input("Enter the Position : "))
                    if 0 <= s1 < len(lst):
                        del lst[s1]
                    else:
                        print("Invalid Position")
                    print("After deletion the list: ",lst)
                    c = input("Do you Want to continue the process?(Y/N) ")
                    if (c.lower()=="n"):
                        break
            else:
                print("Enter the Valid Option")
        elif(cho == 3):
            print(" "*11,"  DISPLAY  ","*"*11)
            print("The List is : ",lst)
        elif (cho == 4):
            print("="*10," GAME OVER","="*10)
            break
        else : 
            if (cho.isdigit()==False):
                print(" "*11,"  NOT VALID  ","*"*11)
            else:
                print("Enter a Valid integer")

'''
# 400
'''
lst = eval(input("Enter the List: "))

u_lst = []
d_lst = []

for a in lst:
    count = lst.count(a)
    print("Element", a, "frequency:", count)

    if count == 1:
        if a not in u_lst:
            u_lst.append(a)
    else:
        if a not in d_lst:
            d_lst.append(a)

print("Original list:", lst)
print("Unique list:", u_lst)
print("Duplicate list:", d_lst)
'''

# 407 problem 17
'''L = [12,23,45,16,22,34]
for i in range(0,len(L),2):
    print(i,"-->",i+1)
    L[i],L[i+1] = L[i+1],L[i]
print("List after swapping: ",L)'''

#408 problem 22
'''
lst = eval(input("Enter the List: "))
lst.sort(reverse = True)
print("The second largest Number is : ",lst[1])'''

# SORT A LIST WITHOUT FUNCTION SORT

'''
lst = [23, 12, 16, 45, 34, 22]
srt = []

while lst:
    k = max(lst)
    srt.append(k)
    lst.remove(k)

print("The Sorted list in Descending order is:", srt)
'''

'''
lst = eval(input("Enter the List: "))

for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] > lst[j]:
            lst[i], lst[j] = lst[j], lst[i] 

print("Ascending order:", lst)

'''