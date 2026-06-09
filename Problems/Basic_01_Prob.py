L_name = []
L_age = []
L_dept = []
def add_student(no):
    for i in range(no):
        print("Enter the Details of student ",i+1)
        name = input("Enter the Name : ")
        Age = int(input("Enter the Age : "))
        Dept = input("Enter the Department : ")
        print()
        L_name.append(name)
        L_age.append(Age)
        L_dept.append(Dept)

def search_student(no):
    for i in range(no):
        nme = input("Enter the Student Name")
        for j in range(len(L_name)):
            if (str(L_name[i]).lower() == nme.lower()):
                print(j+1,".",L_name[j]," | ",L_age[j]," | ",L_dept[j])

def View_students():
    for j in range(len(L_name)):
        print(j+1,".",L_name[j]," | ",L_age[j]," | ",L_dept[j])

def delete_students(n):
    for i in range(len(L_name)):
        if n in L_name[i]:
            L_name.pop(i)
            L_age.pop(i)
            L_dept.pop(i)

def main ():
    while True :
        print("*"*12,"RECORD MANAGER","*"*12)
        print("Your Options (Choose one) :")
        print(" "*5,"1. ADD a Student")
        print(" "*5,"2. VIEW a Student Detail")
        print(" "*5,"3. SEARCH Student")
        print(" "*5,"4. DELETE a Student")
        print(" "*5,"5. EXIT")
        cho = int(input("Enter the Choice Number : "))
        if (cho == 1):
            no = int(input("Enter How Many students ?: "))
            add_student(no)
        if (cho == 2):
            View_students()
        if (cho == 3):
            no = int(input("Enter How Many students ?: "))
            search_student(no)
        if (cho == 4):
            nme = input("Enter the Student Name to Delete : ")
            delete_students(nme)
        if (cho == 5):
            print("Exiting......")
            print("Exited Successfully")
            break
main()