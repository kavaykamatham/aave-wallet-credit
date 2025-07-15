# 🏦 Aave Wallet Credit Scoring

This project builds a machine learning pipeline to assign credit scores (0–1000) to wallets on the Aave V2 protocol using historical transaction data.

## 📌 Objective

Analyze user-level DeFi transactions and compute a **credit score** per wallet based on behavioral patterns, risk factors, and activity levels.

## 📁 Project Structure

```
aave-wallet-credit/
├── data/
│   ├── user-transactions.json         # Raw JSON transaction data (87MB)
│   ├── txns.parquet                   # Cleaned parquet version
│   └── features.parquet               # Engineered features
│
├── src/
│   ├── load_data.py                   # JSON → Parquet converter
│   ├── feature_engineering.py         # Creates wallet features
│   ├── train_model.py                 # Trains model & scaler
│   ├── score.py                       # Scores wallets using trained model
│   ├── analysis.py                    # Generates plots from scored results
│   ├── models/
│   │   ├── credit_model.pkl           # Trained model
│   │   └── scaler.pkl                 # Scaler used for prediction
│   └── assets/                        # Saved analysis visualizations
│
├── scored.csv                         # Wallets with credit scores
├── analysis.md                        # Visual & behavioral insights
├── README.md                          # This file
├── requirements.txt                   # Python dependencies
└── .gitignore
```

---

## 🚀 How to Run

### 1️⃣ Install requirements

```bash
pip install -r requirements.txt
```

### 2️⃣ Convert raw JSON to Parquet

```bash
python src/load_data.py --input data/user-transactions.json --output data/txns.parquet
```

### 3️⃣ Feature Engineering

```bash
python src/feature_engineering.py
```

### 4️⃣ Train ML Model

```bash
python src/train_model.py --input data/features.parquet
```

### 5️⃣ Score Wallets

```bash
python src/score.py --input data/features.parquet --output scored.csv
```

### 6️⃣ Generate Visual Analysis

```bash
python src/analysis.py
```

---

## 📊 Scoring Strategy

Features used:
- `txn_count`, `active_days`
- Total & number of actions (`deposit`, `borrow`, `repay`, `redeem`, `liquidations`)
- `liquidation_flag`

Model used:
- `RandomForestRegressor`
- Output scaled between 0–1000

---

## 📈 Score Interpretation

| Score Range | Interpretation              |
|-------------|-----------------------------|
| 0–200       | Risky, suspicious, bot-like |
| 200–600     | Moderate risk               |
| 600–800     | Reliable users              |
| 800–1000    | Highly trustworthy wallets  |

---

## 📎 Submission Files

- `README.md` — this file
- `analysis.md` — wallet score insights & plots
- `scored.csv` — final credit scores

---

## ✅ Author

**Kavya Kamatham**  
GitHub: [@kavaykamatham](https://github.com/kavaykamatham)

---

## 🔗 References

- [Aave V2 Protocol](https://docs.aave.com/)
- JSON file: [User Transactions (Google Drive)](https://drive.google.com/file/d/1ISFbAXxadMrt7Zl96rmzzZmEKZnyW7FS/view)
