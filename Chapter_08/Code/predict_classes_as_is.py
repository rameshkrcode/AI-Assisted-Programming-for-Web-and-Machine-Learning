y_pred = model.predict(X_test)
y_pred_classes = (y_pred > 0.5).astype("int32")