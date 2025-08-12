
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators=100, max_depth=8, class_weight='balanced')
model.fit(X_train, y_train)
