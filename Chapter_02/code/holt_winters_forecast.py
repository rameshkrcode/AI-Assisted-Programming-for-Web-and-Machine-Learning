
from statsmodels.tsa.holtwinters import ExponentialSmoothing

model = ExponentialSmoothing(data["consumption"], seasonal="add", seasonal_periods=24).fit()
forecast = model.forecast(steps=48)
print(forecast)
