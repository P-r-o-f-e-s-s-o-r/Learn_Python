#STUDENTS PERFORMANCE ANLYZER
#Build a program that analyzes marks of students and generates a report.

import numpy as np
students = []
marks = list(students[1:])

def stu_details(no):
    for i in range(no):
        Name = input("Enter the Name of the Student : ")
        m1 = int(input("Enter the Sub 1 Mark : "))
        m2 = int(input("Enter the Sub 1 Mark : "))
        m3 = int(input("Enter the Sub 1 Mark : "))
        Data = [Name.lower(),m1,m2,m3]
        students.append(Data)

def calculate_average(marks):
    o_avg = np.array(marks)
    avg = np.mean(o_avg)
    return avg
def find_grade(avg):
    if (avg>90):
        grade = "A"
    elif (avg>80 and avg<90):
        grade = "B"
    elif (avg>70 and avg<80):
        grade = "C"
    elif (avg>60 and avg<70):
        grade = "D"
    elif (avg<60):
        grade = "F"
    else:
        grade = 0
    return grade

def generate_report():
    grade = find_grade()
    avg = calculate_average()
    for i in range(len(students)):
        print("Name"," "*4,"Average"," "*4,"Grade")
        print("-"*20)
        print(students[i][0]," "*4,avg," "*4,grade)


def main():
    while True:
        print("*"*5,"STUDENTS PERFORMANCE ANALYZER","*"*5)
        print(" "*5,"1. ADD STU DETAILS")
        print(" "*5,"2. CALCULATE AVG MARK")
        print(" "*5,"3. FIND GRADE")
        print(" "*5,"4. GENERATE REPORT")
        print(" "*5,"5. EXIT")
        cho = int(input("Enter the Choice : "))
        if (cho == 1):
            no = int(input("Enter The Number Of Students :"))
            stu_details(no)
        if (cho == 2):
            if(len(students) == 0):
                print("First add student Details ")
            else:
                avg = calculate_average(marks)
                print("The Average is : ",avg)
                print("Calculation of Avg is Completed...")
                print("Exiting....")
                break
        if (cho == 3):
            if(len(students) == 0):
                print("First add student Details ")
            else:
                avg = calculate_average()
                grade = find_grade(avg)
                print("The Grade is : ",grade)
                print("Finding grade is Completed...")
                print("Exiting....")
                break
        if (cho == 4):
            if(len(students) == 0):
                print("First add student Details ")
            else:
                generate_report()
                print("Calculation of Avg is Completed...")
                print("Exiting....")
                break
        if (cho == 5):
            print("Analyse is Completed...")
            print("Exiting....")
            break

main()
