#340 problem Simple
'''
num = int(input("Enter The Number: "))
st = str(num)
if "0" in st:
    print("The 0 is present in ",num)
else:
    print("No 0 is present in ",num)
'''
#341 
'''
uname = input("Enter the Name: ")
code = input("Enter the code: ")
if uname in code:
    print("Enter a Valid Code")
else:
    print("You code is accepted..")
'''

# STRING SLICING..
'''
word = "amazing"

print(word[0:len(word)])
print(word[-7:-3])
print(word[3:]+word[:3])
print(word[:3]+word[3:])
print(word[1:6:2])
print(word[-7:-3:3])
print(word[::-2])
print(word[::-1])
'''
#344 
'''
s1 = input("Enter the Word 1 : ")
s2 = input("Enter the Word 2 : ")

if s1 in s2:
    s3 = s2[0:4] + "Restore"
else:
    s3 = s2
print("The orginal: ",s1,s2)
print("The Final : ",s1,s3)
'''

#358
'''
word = input("Enter The word: ")
Aword = word.title()
print("The Original word :",word)
print("The Original Aword :",Aword)
'''
#359                                           # INCOMPLETE
'''word = input("Enter The Word: ")
length = len(word)
maxsub = 0
sub =[]
k = word.split()
for a in range(length):
    for i in k:
        lensub = len(k[a])
        sub.append(lensub)
  '''      

# PAGE NO 358 TO 361 HAVE GOOD PROBLEMS CHECK IT OUT