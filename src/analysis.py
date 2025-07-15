import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

ASSET_DIR = "assets"
os.makedirs(ASSET_DIR, exist_ok=True)

def plot_all(scored_path):
    print("📂 Loading scored.csv...")
    df = pd.read_csv(scored_path)

    if "credit_score" not in df.columns:
        raise KeyError("Expected 'credit_score' column not found.")

    # Binning scores for grouped analysis
    df["score_bin"] = pd.cut(
        df["credit_score"], 
        bins=[0,100,200,300,400,500,600,700,800,900,1000],
        labels=["0-100","100-200","200-300","300-400","400-500",
                "500-600","600-700","700-800","800-900","900-1000"]
    )

    # Load features for merged analysis
    try:
        features = pd.read_parquet("../data/features.parquet")
    except:
        print("⚠️ Could not read features.parquet.")
        return

    # Merge on wallet
    merged = pd.merge(df, features, on="wallet", how="left")

    required_cols = {"credit_score", "txn_count", "liquidation_flag", "score_bin"}
    if not required_cols.issubset(set(merged.columns)):
        print("⚠️ Required columns not found in features.parquet for merged plots.")
        return

    # Plot 1: Raw Score Distribution
    plt.figure(figsize=(8,5))
    sns.histplot(df["credit_score"], bins=30, kde=False)
    plt.title("Score Distribution")
    plt.xlabel("Credit Score")
    plt.ylabel("Count")
    plt.savefig(f"{ASSET_DIR}/score_distribution.png")
    plt.close()

    # Plot 2: KDE (Smoothed) Score Distribution
    plt.figure(figsize=(8,5))
    sns.histplot(df["credit_score"], bins=30, kde=True, stat="density")
    plt.title("KDE Smoothed Score Histogram")
    plt.xlabel("Credit Score")
    plt.ylabel("Density")
    plt.savefig(f"{ASSET_DIR}/smooth_score_hist.png")
    plt.close()

    # Plot 3: Average txn_count per score_bin
    avg_activity = merged.groupby("score_bin")["txn_count"].mean().reset_index()
    plt.figure(figsize=(8,5))
    sns.barplot(data=avg_activity, x="score_bin", y="txn_count", palette="Blues_d")
    plt.title("Avg. Transactions per Score Bin")
    plt.xlabel("Score Bin")
    plt.ylabel("Average Transactions")
    plt.savefig(f"{ASSET_DIR}/avg_activity_per_score_bin.png")
    plt.close()

    # Plot 4: Scatter – Transactions vs Score
    plt.figure(figsize=(8,5))
    sns.scatterplot(data=merged, x="credit_score", y="txn_count", alpha=0.5)
    plt.title("Transactions vs Credit Score")
    plt.xlabel("Credit Score")
    plt.ylabel("Transaction Count")
    plt.savefig(f"{ASSET_DIR}/action_vs_score.png")
    plt.close()

    # Plot 5: Liquidation rate by score bin
    liquidation_rate = merged.groupby("score_bin")["liquidation_flag"].mean().reset_index()
    plt.figure(figsize=(8,5))
    sns.barplot(data=liquidation_rate, x="score_bin", y="liquidation_flag", palette="Reds_d")
    plt.title("Avg. Liquidation Rate per Score Bin")
    plt.xlabel("Score Bin")
    plt.ylabel("Liquidation Rate")
    plt.savefig(f"{ASSET_DIR}/liquidation_flags.png")
    plt.close()

    print("[✅] All plots generated and saved in 'assets/'")

if __name__ == "__main__":
    plot_all("../scored.csv")
