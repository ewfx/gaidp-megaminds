import pandas as pd
from sklearn.ensemble import IsolationForest

def detect_anomalies(data):
    """Use Isolation Forest to detect anomalies in transactions."""
    features = ["Transaction Amount", "Reported Amount", "Account Balance"]
    
    model = IsolationForest(contamination=0.05, random_state=42)
    model.fit(data[features])
    
    data["Anomaly"] = model.predict(data[features])  # -1 = Anomaly, 1 = Normal
    return data

if __name__ == "__main__":
    df = pd.read_csv("data/transactions.csv")
    df = detect_anomalies(df)
    print(df.head())  # Show results
