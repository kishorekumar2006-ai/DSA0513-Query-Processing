import pandas as pd
df = pd.read_csv("P7.csv")
table = pd.pivot_table(
    df,
    values="Sale_amt",
    index="Item",
    aggfunc=["max", "min"]
)
print(table)