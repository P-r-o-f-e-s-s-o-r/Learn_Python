import pandas as pd

#SERIES 
#/////////////////////////////////////////////
#age = [23,42,1,31]
'''
series = pd.Series(age)
print(series)
'''
#Using Index to Access the Element 
'''
print(series.loc[1])
print(age[1])
'''
#Manual Assigning Index Value 
'''
series = pd.Series(age, index = ["A","B","C","D"])
print(series.loc["A"])
print(series)
print(age[1])
'''

#Convert Dictionary to Series 
age = {
    "Mukesh": 18,
    "Taazim": 19,
    "giri": 19
}
series = pd.Series(age)
print(series)
print(series[series>18])
#/////////////////////////////////////////////

#DATAFRAME

#/////////////////////////////////////////////

students = {
    "Name" : ["Goms","Siva","Code io"],
    "Age" : [25,22,5],
    "CGPA" : [8.5,10,5]
}

df = pd.DataFrame(students,index=["std 1","std 2","std 3"])
#print(df)
'''
print(df.loc["std1"])
print(df.iloc["std1"])
'''
df["Medium"] = ["English","Tamil","Telugu"] #ADDING NEW COLUMN
print(df)

std4 = pd.DataFrame({"Name" : ["Undefined"] , "Age": [2] , "CGPA" : [10] } , index = ["std 4"]) #ROW Creation
df = pd.concat([df,std4])
print(df)
#/////////////////////////////////////////////