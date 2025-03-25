from sklearn.ensemble import IsolationForest
import numpy as np
import pandas as pd

def risk_scoring(data):
    model = IsolationForest(contamination=0.05)
    risk_scores = model.fit_predict(data.select_dtypes(include=[np.number]))
    
    data["Risk_Score"] = risk_scores
    return data
