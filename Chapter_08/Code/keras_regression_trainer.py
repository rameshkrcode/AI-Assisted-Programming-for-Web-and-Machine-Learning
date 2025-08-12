from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
# Define the regression model
model = Sequential([
    Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    Dropout(0.2),  # Helps prevent overfitting
    Dense(64, activation='relu'),
    Dense(1)  # No activation function for continuous output
])
# Compile the model with regression-specific loss and metrics
model.compile(
    optimizer='adam',
    loss='mse',           # Mean Squared Error for regression
    metrics=['mae']       # Mean Absolute Error as an additional metric
)
# Train the model with early stopping
model.fit(
    X_train, y_train,
    epochs=50,
    validation_split=0.2,
    callbacks=[early_stop]
)
