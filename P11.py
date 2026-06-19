import pandas as pd
df = pd.read_csv("P11.csv")
def highlight(x):
    if pd.isna(x):
        return "background-color:yellow"
    else:
        return ""
df.style.map(highlight)