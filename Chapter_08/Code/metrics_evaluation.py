from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import numpy as np
# Predictions
preds = lr.predict(X_test)
# Evaluation metrics
print("MAE:", mean_absolute_error(y_test, preds))
print("MSE:", mean_squared_error(y_test, preds))
print("RMSE:", np.sqrt(mean_squared_error(y_test, preds)))
print("R^2:", r2_score(y_test, preds))