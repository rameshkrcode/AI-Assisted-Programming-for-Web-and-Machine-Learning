
from sklearn.feature_selection import SelectFromModel
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
selector = SelectFromModel(model)
X_selected = selector.fit_transform(X, y)
