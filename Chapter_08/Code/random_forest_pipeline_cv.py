
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', RandomForestClassifier(n_estimators=200, max_depth=10, random_state=42))
])
scores = cross_val_score(pipeline, X, y, cv=5, scoring='f1')
print("Average F1 Score:", scores.mean())
