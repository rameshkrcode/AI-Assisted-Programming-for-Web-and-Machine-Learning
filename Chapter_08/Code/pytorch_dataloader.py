
from torch.utils.data import DataLoader, TensorDataset
from sklearn.preprocessing import StandardScaler
import torch

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

dataset = TensorDataset(torch.tensor(X_train_scaled, dtype=torch.float32),
                        torch.tensor(y_train, dtype=torch.float32))

loader = DataLoader(dataset, batch_size=32)
