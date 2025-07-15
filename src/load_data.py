import argparse, pathlib, json
import pandas as pd
from tqdm import tqdm


def load_json_to_df(path: str) -> pd.DataFrame:
    print(f"[📂] Loading JSON file → {path}")
    with open(path, "r", encoding="utf-8") as f:
        records = json.load(f)

    df = pd.DataFrame.from_records(records)

    # Rename userWallet to wallet
    df.rename(columns={"userWallet": "wallet"}, inplace=True)

    # Convert timestamp to datetime
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")

    # Extract numeric amount (if present) from actionData field
    def extract_amount(x):
        if isinstance(x, dict) and "amount" in x:
            try:
                return float(x["amount"]) / 1e18  # Convert from wei to ETH
            except:
                return 0
        return 0

    df["amount"] = df["actionData"].apply(extract_amount)

    print(f"[✅] Loaded {len(df):,} rows with shape {df.shape}")
    return df


def cli():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--output", default="data/txns.parquet")
    args = ap.parse_args()

    df = load_json_to_df(args.input)
    pathlib.Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(args.output, index=False)
    print(f"[✅] Saved tidy parquet → {args.output}")


if __name__ == "__main__":
    cli()
