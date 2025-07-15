# Wallet Credit Score Analysis

## 🔢 Score Distribution Overview

We scored 3,497 unique wallets with credit scores ranging from **0 to 1000**, reflecting their interaction patterns with the Aave V2 protocol.

### 📊 Score Distribution
![Score Distribution](assets/score_distribution.png)

- The majority of wallets are concentrated in the **0–200 score range**.
- A sharp drop is observed beyond the 300 mark.
- Very few wallets score **above 800**, indicating strict scoring logic favoring responsible behavior.

---

## 🔁 Smoothed Score Histogram (KDE)
![KDE Histogram](assets/smooth_score_hist.png)

- Shows a **sharp spike near 0**, confirming a significant number of wallets with poor creditworthiness.
- The curve smooths toward higher scores, suggesting fewer wallets exhibit ideal behavior.

---

## 📉 Average Activity per Score Band
![Activity per Score Band](assets/avg_activity_per_score_bin.png)

- Wallets in **higher score ranges (800–1000)** have **significantly higher activity**, including more transactions and active days.
- Lower-scoring wallets (0–200) are generally less engaged or perform limited actions.

---

## 📈 Total Actions vs Credit Score
![Actions vs Score](assets/action_vs_score.png)

- A clear upward trend is visible: **more actions typically yield higher credit scores**.
- This supports the idea that the model rewards **consistent protocol usage**.

---

## ⚠️ Liquidation Rate by Score Bin
![Liquidation Flags](assets/liquidation_flags.png)

- A **high percentage of wallets in the 0–200 range have faced liquidations**.
- In contrast, **wallets with scores >800** almost never get liquidated, showing **strong asset management and repayment discipline**.

---

## 🧠 Behavioral Insights

### 🔻 Low-Scoring Wallets (0–300)
- Often have:
  - Very few transactions.
  - High incidence of liquidation.
  - Low repayment or redeem activity.
- May represent:
  - Bots or spam wallets.
  - Risky borrowing with poor repayment behavior.
  - Inactive wallets with minimal interaction.

### 🔼 High-Scoring Wallets (800–1000)
- Typically:
  - Interact frequently with Aave.
  - Borrow, repay, and redeem responsibly.
  - Avoid liquidation altogether.
  - Stay active across multiple days.

- These wallets indicate:
  - Human-controlled, healthy financial behavior.
  - Consistency, reliability, and risk aversion.

---

## ✅ Summary

The model successfully distinguishes between responsible and risky users using transaction patterns. It prioritizes:

- **Frequency** and **consistency** of activity.
- **Avoidance of liquidation**.
- **Balanced borrowing and repayment behaviors**.

These features are crucial in assigning fair credit scores for DeFi protocols like Aave.

