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