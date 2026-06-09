print("*"*10,"PASSWORD ANALYZER","*"*10)
print()
pas = input("Enter The Password: ")
def main():
    def check_L():
        L = len(pas)
        return L
    def check_upper():
        for i in pas:
            if (i.isupper()):
                count = 1
                break
            else:
                count = 0
        return count
    def check_Lower():
        for i in pas:
            if (i.islower()):
                count = 1
                break
            else:
                count = 0
        return count
    def check_Num():
        for i in pas:
            if (i.isdigit()):
                count = 1
                break
            else:
                count = 0
        return count
    def check_Speacial():
        for i in pas:
            if (i in "@#$%&*!"):
                count = 1
                break
            else:
                count = 0
        return count
    def Analyze_Pas():
        Len = check_L()
        r1 = check_upper()
        r2 = check_Lower()
        r3 = check_Num()
        r4 = check_Speacial()
        Li = [r1,r2,r3,r4]
        for i in range(len(Li)):
            if (Len>=8):
                if (Li [i] == 0 ):
                    print ("Password Strength is : weak")
                    print("ANALYSATION COMPLETED")
                    break
                elif(Li[i] == 1):
                    print("Password Strength is : strong")
                    print("ANALYSATION COMPLETED")
                    break
                else:
                    print("Some Error occured")
                    break
            else:
                print ("Password Strength is : weak")
                print("ANALYSATION COMPLETED")
                break
    Analyze_Pas()
main()