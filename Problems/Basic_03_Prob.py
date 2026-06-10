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
'''
Cat = []
Amt = [] 

def add_exp(n):
    for i in range(n):
        cat = input("Enter the Category : ")
        amt = int(input("Enter the Amount : "))
        print()
        Cat.append(cat.lower())
        Amt.append(amt)

def view_exp(ch):
    K = ch
    if (K.lower() == "all"):
        for i in range(len(Cat)):
            print(Cat[i].capitalize(), " : Rs", Amt[i])
    if (K.lower() == "particular"):
        s = input("Enter the Category to search : ")
        for i in range(len(Cat)):
            if (s.lower() == Cat[i]):
                print(Cat[i].capitalize(), " : Rs", Amt[i])

def cal_total():
    if not Amt:
        print("No expenses recorded yet.")
        return
        
    total = 0
    print("\n| Category : Expenses |")
    print("-------------------------")
    for i in range(len(Amt)):
        total += Amt[i]
        print(f"| {Cat[i].capitalize()} : Rs {Amt[i]} |")
        
    print("-----------------------------")
    print(f"The Total Expenses : Rs {total}") # Fixed: Now correctly displays the total
    print("-----------------------------")

def del_exp():
    s = input("Enter the Category to delete : ")
    i = 0
    deleted = False
    # Using a while loop prevents index errors when modifying the list size dynamically
    while i < len(Cat):
        if s.lower() == Cat[i]:
            Cat.pop(i)
            Amt.pop(i)
            deleted = True
            # Do not increment 'i' here because the next item shifted into the current index
        else:
            i += 1
            
    if deleted:
        print(f"All expenses under '{s}' have been deleted.")
    else:
        print("Category not found.")


def main():
    while True:
        print("\n" + "*"*10, "EXPENSE TRACKER", "*"*10)
        print(" "*5, "1 . ADD EXPENSES")        
        print(" "*5, "2 . VIEW EXPENSES")
        print(" "*5, "3 . CALCULATE EXPENSES")
        print(" "*5, "4 . DELETE EXPENSES")
        print(" "*5, "5 . EXIT")
        print()
        
        try:
            cho = int(input("Enter the Choice : "))
        except ValueError:
            print("Please enter a valid number.")
            continue
            
        if cho == 1:
            no = int(input("Number of Expenses : "))
            add_exp(no)
        elif cho == 2:
            ch = input("Want to View all or particular? : ")
            view_exp(ch)
        elif cho == 3:
            cal_total()
        elif cho == 4:
            del_exp()
        elif cho == 5:
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please select 1-5.")

# CRITICAL FIX: You must call the main function to start the program
if __name__ == "__main__":
    main()
'''