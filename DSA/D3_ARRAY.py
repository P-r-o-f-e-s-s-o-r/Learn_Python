#Find the Largest and Smallest Number 

'''while True:
    arr = eval(input("Enter The List: "))

    largest = arr[0]
    smallest = arr[0]

    for i in arr:
        if i > largest:
            largest = i
        if i < smallest:
            smallest = i

    print("The Largest Number in The List is :", largest)
    print("The Smallest Number in The List is :", smallest)

    cho = input("Do you want to Continue? (Y/N): ")
    if cho.lower() == "n":
        break
'''
'''while True:
    arr = eval(input("Enter The List: "))
    for i in range(len(arr)):
        for a in arr:
            if a > arr[i]:
                max = arr[i]
            elif a < arr[i]:
                min = a
    print("The Largest Number in The List is : ",max)
    print("The smallest Number in The List is : ",min)
    cho = input("Do you want to Continue?(Y/N): ")
    if cho.lower()=="n":
        break'''

#FINDING SECOND LARGEST ELEMENT
'''while True:
    lst = eval(input("Enter the list: "))

    # Sort the list (ascending)
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]

    first = lst[-1]          # largest element

    # Find second largest
    for i in range(len(lst)-2, -1, -1):                      #DOUBT PART
        print(i)
        if lst[i] != first:
            second = lst[i]
            break

    print("The Second Largest Number is :", second)

    cho = input("Do you want to Continue?(Y/N): ")
    if cho.lower() == "n":
        break
'''
'''while True:
    arr = eval(input("Enter The List: "))

    largest = arr[0]
    second = arr[0]

    for i in arr:
        if i > largest:
            largest = i
            second = largest
            if largest > second :
                second = second


    print("The Largest Number in The List is :", largest)
    print("The Second Number in The List is :", second)

    cho = input("Do you want to Continue? (Y/N): ")
    if cho.lower() == "n":
        break
'''

# CHECK IF ARRAY IS SORTED
'''while True:
    arr = eval(input("Enter The List: "))

    largest = arr[0]
    smallest = arr[0]

    for i in arr:
        if i > largest:
            largest = i
        if i < smallest:
            smallest = i
    arr.sort()
    output = 0
    print(arr)
    if (arr[-1]==largest and arr[0]==smallest):
        output = True
    else:
        output = False

    print(output)
    cho = input("Do you want to Continue? (Y/N): ")
    if cho.lower() == "n":
        break
'''
'''
while True:
    arr = eval(input("Enter The List: "))
    output = 0
    print(arr)
    for i in range (1,len(arr)):
        if (arr[i]<arr[i-1]):
            output = False
        else:
            output = True

    print(output)
    cho = input("Do you want to Continue? (Y/N): ")
    if cho.lower() == "n":
        break
'''

'''while True:
    arr = eval(input("Enter The List: "))
    val = int(input("Enter The Number: "))
    arr.sort()
    while (val in arr):
        arr.remove(val)
    k = len(arr)
    print("the final array :",k)

    cho = input("Do you want to Continue? (Y/N): ")
    if cho.lower() == "n":
        break'''

#REVERSE A ARRAY OR STRING  [IN PLACE : Not alternating the orignail or copying ] 
'''class Solution(object):
    def reverseString(self, s):
        left = 0
        right = len(s) - 1
        
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1'''

#remove-duplicates-from-sorted ARRAY
'''while True:
    arr = eval(input("Enter The Sorted List: "))

    i = 1
    while i < len(arr):
        if arr[i] == arr[i - 1]:
            arr.pop(i)
        else:
            i += 1

    print(arr)
    print("The Length of Array is :", len(arr))

    cho = input("Do you want to Continue? (Y/N): ")
    if cho.lower() == "n":
        break'''
'''
while True: 
    arr = eval(input("Enter The List: "))
    for a in range(len(arr)):
        for i in arr:
            c_count = arr.count(i)
            if (c_count>=2):
                arr.remove(arr[a])
    k = len(arr)
    print(arr)
    print("The Length of Array is : ",k)

    cho = input("Do you want to Continue? (Y/N): ")
    if cho.lower() == "n":
        break'''