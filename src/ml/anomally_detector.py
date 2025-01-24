import joblib
import numpy as np
from sklearn.ensemble import IsolationForest
from config.settings import Config

class AnomalyDetector:
    def __init__(self):
        self.model = self.load_model()
        
    def load_model(self):
        try:
            return joblib.load(f"{Config.MODEL_PATH}/model.pkl")
        except FileNotFoundError:
            return IsolationForest(n_estimators=100, contamination=0.01)

    def preprocess(self, transaction):
        return np.array([[transaction['amount'], transaction.get('frequency', 0)]])
    
    def is_anomalous(self, transaction):
        features = self.preprocess(transaction)
        score = self.model.decision_function(features)[0]
        return score < -0.5
