import pandas as pd

df = pd.read_csv('big-mac-full-index.csv')

# Using iterrows() method
for i,r in df.iterrows():
    print(r['currency_code'],
          r['local_price'])

# Using apply() method
print(df.apply(lambda row: row["name"], axis = 1))