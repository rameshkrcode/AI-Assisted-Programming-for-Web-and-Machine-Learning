
from sklearn.feature_selection import SelectKBest, f_regression
X = df[['Experience', 'Salary']]
y = [0, 1, 1, 0]  # Sample binary target
selector = SelectKBest(score_func=f_regression, k=1)
X_selected = selector.fit_transform(X, y)
