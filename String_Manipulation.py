#ASK USER FOR USERNAME AND PCODE . MAKE SURE THAT PCODE DOESNT CONTAIN USERNAME AND MATCHES "Trident111"
'''
U_name = input("Enter the User Name : ")
pcoode = input("Enter the PASSWORD: ")

if (pcoode not in U_name and pcoode == "Trident111"):
    print("Code is Valid")
else:
    print("Invalid")
'''

#patter Print without Nested loop
'''
for i in range (5):
    print("#"*i) 
'''

#STRING SLICING 
'''
w = "amazing"

print(w[2:])
print(w[:2])
print(w[4:]+w[:4])
print(w[:4]+w[4:])
print(w[-5:-1])
print(w[1:6:2])
print(w[-7:-3:3])
print(w[::-2])
print(w[::-1])
'''

#RESULT
'''
azing
am
ingamaz
amazing
azin
mzn
az
giaa
gnizama
'''

#PALINDROME
'''
st_n = int(input("Enter the Number: "))
st_s= input("Enter the Word: ")

num = str(st_n)
if (num == num[::-1]):
    print(st_n , "Is a Palindrom")
else:
    print(st_n,"Its Not a Palindrom")

if (st_s == st_s[::-1]):
    print(st_s , "Is a Palindrom")
else:
    print(st_s,"Its Not a Palindrom")
'''

#Split Func
'''
k = "I Will Become a Billionaire"
d = k.split()
m = k.split("o")

print(k)
print(d)
print(m)
'''

#FIND No of uppercase , lowercase , digit , space in a word
'''

line = input("Enter the Line: ")
c_up = c_lo = 0
c_d = c_s = 0

# Iterate through each character in the string one by one
for char in line:
    if char.isupper():
        c_up += 1
    elif char.islower():
        c_lo += 1
    elif char.isdigit():
        c_d += 1
    elif char.isspace():
        c_s += 1

print("The Number of Uppercase :", c_up)
print("The Number of Lowercase :", c_lo) # Fixed to print c_lo
print("The Number of Digit :", c_d)
print("The Number of Space :", c_s)
'''
