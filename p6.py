import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("P6.csv")
df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)
data = df[(df["Date"] >= "2020-04-01") &
          (df["Date"] <= "2020-05-01")]
plt.scatter(data["Volume"], data["Close"])
plt.title("Alphabet Stock Data")
plt.xlabel("Volume")
plt.ylabel("Close Price")
plt.show()