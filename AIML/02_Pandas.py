import pandas as pd
df = pd.read_csv("customers-100.csv")
#print(df)
print(df["City"].to_string()) # Print Every City