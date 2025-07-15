import argparse
import pandas as pd
import joblib
import pathlib

def score_wallets(df: pd.DataFrame, model_path: str, scaler_path: str):
    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)

    features = df.drop(columns=["wallet"])
    scores = model.predict(features)

    df["credit_score"] = scores.round().clip(0, 1000).astype(int)
    return df[["wallet", "credit_score"]]

def cli():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--model", default="models/credit_model.pkl")
    ap.add_argument("--scaler", default="models/scaler.pkl")
    ap.add_argument("--output", required=True)
    args = ap.parse_args()

    print(f"[📂] Loading features from → {args.input}")
    df = pd.read_parquet(args.input)

    scored_df = score_wallets(df, args.model, args.scaler)

    pathlib.Path(args.output).parent.mkdir(exist_ok=True, parents=True)
    scored_df.to_csv(args.output, index=False)
    print(f"[✅] Saved wallet scores → {args.output}")

if __name__ == "__main__":
    cli()
