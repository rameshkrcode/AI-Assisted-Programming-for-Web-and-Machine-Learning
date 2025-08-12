loss, accuracy = model.evaluate(train_ds)
print(f"Model accuracy: {accuracy * 100:.2f}%")
