
'''k = int(input("Enter The Number :"))
if (k&1==1):
    print("Its a Odd Number")
else:
    print("Its a Even Number")'''


'''arr = [2,3,4,2,3]
unique =0
for a in arr:
    unique =a ^ unique
print(unique)'''

'''n = int(input("Enter The Number : "))
i = 0
Sums =0
while(n>0):
    last = n&1
    n = n>>1
    i+=1
    Sums += last * (5**i)

print(Sums)'''



'''
import math
n = 3475
b = 10

val = int(math.log(n,b)) + 1
print(val)
'''

#CREATE 2D MATRIX
word = input("Enter the elements separated by space: ")
L = word.split()
s_word = input("Enter the word/number to search: ")

if s_word in L:
    index = L.index(s_word)
    print("The Word is Found at Index :", index)
else:
    print("Word Not Found")