from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
# Stop training when validation loss stops improving for 5 consecutive epochs
early_stop = EarlyStopping(patience=5, restore_best_weights=True)
# Save the model only when it achieves a new best on the validation set
checkpoint = ModelCheckpoint('best_model.h5', save_best_only=True)
# Train the model
model.fit(
    X_train, y_train,
    epochs=50,
    batch_size=32,
    validation_split=0.2,
    callbacks=[early_stop, checkpoint]
)
