import pandas as pd
df = pd.read_csv("P12.csv")
df.style.set_properties(**{
    'background-color': 'black',
    'color': 'yellow'
})