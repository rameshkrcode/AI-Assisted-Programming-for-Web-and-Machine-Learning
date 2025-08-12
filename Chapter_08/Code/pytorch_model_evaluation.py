import torch

model.eval()  # Set model to evaluation mode
X_test_tensor = torch.tensor(X_test, dtype=torch.float32).to(device)
y_pred = model(X_test_tensor).detach().cpu().numpy()
y_pred_classes = (y_pred > 0.5).astype(int)
