import argparse
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import MinMaxScaler
import joblib
import pathlib

def generate_pseudo_labels(df):
    """
    Assign synthetic credit scores based on behavior.
    High deposit/repay and low liquidation => high score
    """
    score = (
        df["total_deposit_amt"] * 0.4 +
        df["total_repay_amt"] * 0.3 -
        df["total_liquidated_amt"] * 0.6 -
        df["n_liquidations"] * 10 +
        df["active_days"] * 5
    )
    return score

def train(df: pd.DataFrame, model_path: str, scaler_path: str):
    df["pseudo_score"] = generate_pseudo_labels(df)

    # Normalize score between 0–1000
    scaler = MinMaxScaler(feature_range=(0, 1000))
    df["credit_score"] = scaler.fit_transform(df[["pseudo_score"]])

    features = df.drop(columns=["wallet", "pseudo_score", "credit_score"])
    labels = df["credit_score"]

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(features, labels)

    joblib.dump(model, model_path)
    joblib.dump(scaler, scaler_path)

    print(f"[✅] Model saved → {model_path}")
    print(f"[✅] Scaler saved → {scaler_path}")

def cli():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--model", default="models/credit_model.pkl")
    ap.add_argument("--scaler", default="models/scaler.pkl")
    args = ap.parse_args()

    df = pd.read_parquet(args.input)
    pathlib.Path("models").mkdir(exist_ok=True)
    train(df, args.model, args.scaler)

if __name__ == "__main__":
    cli()
