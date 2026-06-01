#INDEXING A WORD
word = input("Enter the Word : ")
L = list(word)
length = len(L)
print("The List is : ",L)
for i in range(length):
    print("At the Indexes ",i,"and", i-length ," : ",L[i])
