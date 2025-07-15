import pandas as pd

df = pd.read_parquet("../data/txns.parquet")
print("🔎 Columns in txns.parquet:", df.columns.tolist())
print(df.head(3))
