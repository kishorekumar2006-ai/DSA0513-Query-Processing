import pandas as pd
df = pd.read_csv("P10.csv")
def sign(x):
    if x < 0:
        return "Negative"
    else:
        return "Positive"
print(df.map(sign))