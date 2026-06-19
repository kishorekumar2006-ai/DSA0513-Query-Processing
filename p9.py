import pandas as pd

df = pd.read_csv("P9.csv")

print(df.pivot_table(values="Sale_amt",
                     index=["Region","Manager","SalesMan"],
                     aggfunc="sum"))