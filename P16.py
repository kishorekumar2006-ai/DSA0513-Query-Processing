import pandas as pd
df = pd.read_csv("P16.csv")
g = df.groupby("School_Code")
print(g.first())
print(type(g))