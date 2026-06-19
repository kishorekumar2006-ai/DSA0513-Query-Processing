import pandas as pd
df = pd.read_csv("P14.csv")
print(df.fillna("Not Available"))