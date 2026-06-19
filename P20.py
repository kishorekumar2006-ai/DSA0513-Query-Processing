import pandas as pd
df = pd.read_csv("P20.csv")
print(df["Name"].str.find("a"))