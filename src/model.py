from sklearn.ensemble import IsolationForest
import pandas as pd
import joblib
import numpy as np

def build_model(X):
    model = IsolationForest(n_estimators=200, random_state=42)
    model.fit(X)
    return model

def scale_score(scores):
    # Normalize to 0–1000
    lo, hi = np.percentile(scores, [1, 99])
    clipped = np.clip(scores, lo, hi)
    norm = (clipped - lo) / (hi - lo)
    return np.round(norm * 1000).astype(int)

if __name__ == '__main__':
    df = pd.read_csv('data/features.csv')
    X = df.drop(['wallet'], axis=1)
    model = build_model(X)
    joblib.dump(model, 'data/model.joblib')

    scores = model.decision_function(X)
    credit_scores = scale_score(scores)

    df['credit_score'] = credit_scores
    df.to_csv('data/scored_wallets.csv', index=False)
