Cat = []
Amt = [] 
def add_exp(n):
    for i in range(n):
        cat = input("Enter the Catergory : ")
        amt = int(input("Enter the Amount : "))
        print()
        Cat.append(cat.lower())
        Amt.append(amt)

def view_exp(ch):
    K = ch
    if (K.lower() == "all"):
        for i in range(len(Cat)):
            print(Cat[i]," : Rs",Amt[i])
    if (K.lower() == "particular"):
        s = input("Enter the Catergory to search : ")
        for i in range(len(Cat)):
            if (s.lower() == Cat[i]):
                print(Cat[i]," : Rs",Amt[i])

def cal_total():
    total = 0
    for i in range(len(Amt)):
        total+=Amt[i]
        print("| Catergory : Expenses |")
        print("|",Cat[i]," : Rs",Amt[i],"|")
    print("-----------------------------")
    print("The Total Expenses : ")
    print("-----------------------------")

def del_exp():
    s = input("Enter the Catergory to delete : ")
    for i in range(len(Cat)):
        if (s.lower() == Cat[i]):
            Cat.pop(i)
            Amt.pop(i)


def main ():
    while True:
        print("*"*10,"EXPENSE TRACKER","*"*10)
        print(" "*5,"1 . ADD EXPENSES")        
        print(" "*5,"2 . VIEW EXPENSES")
        print(" "*5,"3 . CALCULATE EXPENSES")
        print(" "*5,"4 . DELETE EXPENSES")
        print(" "*5,"5 .  EXIT")
        print()
        cho = int(input("Enter the Choice : "))
        if cho == 1 :
            no = int(input("Number of Expenses : "))
            add_exp(no)
        if cho == 2:
            ch = input("Want to View all or particular? : ")
            if (ch.lower() == "all"):
                view_exp(ch)
            if (ch.lower() == "particular"):
                view_exp(ch)
        if cho == 3:
            cal_total()
        if cho == 4:
            del_exp()
        if cho == 5:
            break
