import argparse, pathlib
import pandas as pd
from tqdm import tqdm


def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    print("[⚙️] Engineering features...")

    # Group by wallet
    grp = df.groupby("wallet")

    # Feature engineering
    features = pd.DataFrame({
        "total_deposit_amt":    grp.apply(lambda x: x[x["action"] == "deposit"]["amount"].sum()),
        "total_borrow_amt":     grp.apply(lambda x: x[x["action"] == "borrow"]["amount"].sum()),
        "total_repay_amt":      grp.apply(lambda x: x[x["action"] == "repay"]["amount"].sum()),
        "total_redeem_amt":     grp.apply(lambda x: x[x["action"] == "redeemunderlying"]["amount"].sum()),
        "total_liquidated_amt": grp.apply(lambda x: x[x["action"] == "liquidationcall"]["amount"].sum()),
        "txn_count":            grp.size(),
        "n_deposit":            grp.apply(lambda x: (x["action"] == "deposit").sum()),
        "n_borrow":             grp.apply(lambda x: (x["action"] == "borrow").sum()),
        "n_repay":              grp.apply(lambda x: (x["action"] == "repay").sum()),
        "n_redeem":             grp.apply(lambda x: (x["action"] == "redeemunderlying").sum()),
        "n_liquidations":       grp.apply(lambda x: (x["action"] == "liquidationcall").sum()),
        "active_days":          grp.apply(lambda x: x["timestamp"].dt.date.nunique())
    })

    # Derived feature
    features["liquidation_flag"] = (features["n_liquidations"] > 0).astype(int)

    print("[✅] Engineered features for", len(features), "wallets.")
    return features.reset_index()


def cli():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--output", required=True)
    args = ap.parse_args()

    print(f"[📂] Loading transactions from: {args.input}")
    df = pd.read_parquet(args.input)

    df_feat = engineer_features(df)

    pathlib.Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    df_feat.to_parquet(args.output, index=False)
    print(f"[💾] Saved features → {args.output}")


if __name__ == "__main__":
    cli()
