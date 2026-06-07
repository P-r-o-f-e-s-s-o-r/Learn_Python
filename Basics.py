#OPERATORS:

'''
print("*"*10," OPERATOR GAME ","*"*10)
a = int(input("Enter The Number a : "))
b = int(input("Enter The Number b : "))
def sum():
    x = a+b
    return x
def sub():
    x = a-b
    return x
def Division():
    try:
        x = a/b
        return x
    except:
        print("Zero Division Error")
        print("*"*10, " GAME OVER ","*"*10)
def FloorDiv():
    x = a//b
    return x
def rem():
    x = a%b
    return x
def multi():
    x = a*b
    return x
def main():
    cho = input("Enter The Symbol of Choice (+,-,%,//,/,*) : ")
    if(cho=="+"):
        sum()
    if(cho=="-"):
        sub()
    if(cho=="%"):
        rem()
    if(cho=="/"):
        Division()
    if(cho=="//"):
        FloorDiv()
    if(cho=="*"):
        multi()
    print("The ",cho," of ",a," and ",b," is :",x)
    print("*"*10, " GAME OVER ","*"*10)
main()
'''

#CORRECTED :
'''
print("*"*10, " OPERATOR GAME ", "*"*10)

a = int(input("Enter The Number a : "))
b = int(input("Enter The Number b : "))

def sum():
    return a + b

def sub():
    return a - b

def Division():
    try:
        return a / b
    except ZeroDivisionError:
        print("Zero Division Error")
        print("*"*10, " GAME OVER ", "*"*10)
        return None

def FloorDiv():
    return a // b

def rem():
    return a % b

def multi():
    return a * b

def main():
    cho = input("Enter The Symbol of Choice (+,-,%,//,/,*) : ")

    if cho == "+":
        x = sum()

    elif cho == "-":
        x = sub()

    elif cho == "%":
        x = rem()

    elif cho == "/":
        x = Division()

    elif cho == "//":
        x = FloorDiv()

    elif cho == "*":
        x = multi()

    else:
        print("Invalid Operator")
        return

    if x is not None:
        print("The", cho, "of", a, "and", b, "is :", x)

    print("*"*10, " GAME OVER ", "*"*10)

main()
'''

#RANDOMS

#HOW RANDOM WORKS 
'''
import random
#print(random.randrange(start,stop,step))
print(random.randrange(1))
'''
'''
import random
num1 = random.randrange(10,70,13)
num2 = random.randrange(10,70,13)
num3 = random.randrange(10,70,13)
set1 = {num1,num2,num3}

print("The Sets : ",set1)
'''

'''

import random
word = input("Enter the Word :")
print(word)
w = list(word)
print(w)
print(len(w))
s = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', 
    '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', 
    '_', '`', '{', '|', '}', '~'
]
for i in range(len(w)):
    print(i)
    K = random.randrange(len(s))
    print(K)
    w[i] = s[K]

F_word = "".join(w)
print("The Cipher text : ", F_word)
'''