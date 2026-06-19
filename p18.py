import pandas as pd
df = pd.read_csv("P18.csv")
print(df.groupby(["School_Code","Class"]).first())