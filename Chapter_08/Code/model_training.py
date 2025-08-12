from sklearn.linear_model import LinearRegression
from sklearn.ensemble import GradientBoostingRegressor
# Initialize models
lr = LinearRegression()
gbr = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1)
# Train models
lr.fit(X_train, y_train)
gbr.fit(X_train, y_train)