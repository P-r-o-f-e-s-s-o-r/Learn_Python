import pandas as pd
#df = pd.read_csv("customers-100.csv")
#print(df)
#print(df["City"].to_string()) # Print Every City
#print(df[["Customer Id","First Name","City"]].to_string()) # Print Every Columns
'''
df = pd.read_csv("customers-100.csv",index_col = "Customer Id") # Make the indexs as CID
#print(df)
print(df.loc["CeD220bdAaCfaDf",["First Name","Last Name"]]) #Particular columns
'''

df = pd.read_json("iris.json")
print(df)
df = df.drop(columns = ["status"]) #DELETE A COLUMN
print(df)
df = df.dropna(subset = ["first_name"]) #Whereever NaN is present it will delete that
print(df)
df["last_name"] = df["last_name"].replace({"Johnson":"john","Brown" : "B"})  # Replace of Particular variable in column
print(df.loc[2])

