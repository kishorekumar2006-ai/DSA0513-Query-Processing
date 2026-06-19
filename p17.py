import pandas as pd
df = pd.read_csv("P17.csv")
print(df.groupby("School_Code")["Age"].agg(["mean","min","max"]))