import pandas as pd
df = pd.read_csv("P8.csv")
table = pd.pivot_table(
    df,
    values="Units",
    index="Item",
    aggfunc="sum"
)
print(table)