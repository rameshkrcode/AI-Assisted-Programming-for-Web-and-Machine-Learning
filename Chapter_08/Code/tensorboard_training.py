from tensorflow.keras.callbacks import TensorBoard
import datetime
# Create a log directory with a timestamp
log_dir = "logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
tensorboard_callback = TensorBoard(log_dir=log_dir, histogram_freq=1)
# Train the model with TensorBoard logging enabled
model.fit(
    X_train, y_train,
    epochs=10,
    validation_split=0.2,
    callbacks=[tensorboard_callback]
)
