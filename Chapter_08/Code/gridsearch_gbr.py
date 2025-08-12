from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import GradientBoostingRegressor
param_grid = {'learning_rate': [0.01, 0.1], 'n_estimators': [100, 200]}
grid = GridSearchCV(GradientBoostingRegressor(), param_grid, cv=5)
grid.fit(X_train, y_train)
print("Best Parameters:", grid.best_params_)
