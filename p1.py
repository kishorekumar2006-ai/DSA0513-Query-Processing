import pandas as pd
df = pd.read_csv("P1.csv")
print(df["DEPARTMENT_ID"].unique())