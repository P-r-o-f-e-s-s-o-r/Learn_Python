#STUDENTS PERFORMANCE ANLYZER
#Build a program that analyzes marks of students and generates a report.

import numpy as np
students = [1,2,3,4]
marks = list(students[1:])

def stu_details(no):
    for i in range(no):
        Name = input("Enter the Name of the Student : ")
        m1 = int(input("Enter the Sub 1 Mark : "))
        m2 = int(input("Enter the Sub 1 Mark : "))
        m3 = int(input("Enter the Sub 1 Mark : "))
        Data = [Name,m1,m2,m3]
        students.append(Data)

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
                calculate_average()
                print("Calculation of Avg is Completed...")
                print("Exiting....")
                break
        if (cho == 3):
            if(len(students) == 0):
                print("First add student Details ")
            else:
                find_grade()
                print("Calculation of Avg is Completed...")
                print("Exiting....")
                break
        if (cho == 4):
            if(len(students) == 0):
                print("First add student Details ")
            else:
                generate_report(students)
                print("Calculation of Avg is Completed...")
                print("Exiting....")
                break
        if (cho == 5):
            print("Analyse is Completed...")
            print("Exiting....")
            break
