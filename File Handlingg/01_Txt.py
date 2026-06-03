'''
file = open("poem.txt","r")
red = file.read(10)   #READ ONLY 10 BYTES
print(red,end="")
red1 = file.read(30) #READ OTHER SET OF LINES
print(red1)

'''

'''
re = file.read()
print(re)
for line in file:
   print(line)
'''

#write
file = open("Names.txt","w")
n = int(input("Number of people : "))
for i in range(n):
    name = input("Enter The Name : ")
    file.write(name)
    file.write("\n")
file.close()