import json, pandas as pd
from tqdm import tqdm

def load_json_to_df(filepath):
    with open(filepath) as f:
        raw_data = [json.loads(line) for line in tqdm(f)]
    df = pd.DataFrame(raw_data)
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
    return df

if __name__ == '__main__':
    df = load_json_to_df('data/user-transactions.json')
    df.to_parquet('data/txns.parquet', index=False)
