
from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd

class DataCleaner(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        X = X.copy()
        X['JoinDate'] = pd.to_datetime(X['JoinDate'], errors='coerce')
        X.columns = X.columns.str.strip().str.lower().str.replace(' ', '_')
        return X
