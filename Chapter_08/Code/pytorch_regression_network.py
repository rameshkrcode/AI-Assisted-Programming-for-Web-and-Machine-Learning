import torch
import torch.nn as nn
class RegressionModel(nn.Module):
    def __init__(self, input_dim):
        super().__init__()
        self.network = nn.Sequential(
            nn.Linear(input_dim, 64),
            nn.ReLU(),
            nn.Linear(64, 64),
            nn.ReLU(),
            nn.Linear(64, 1)
        )
    def forward(self, x):
        return self.network(x)
# Instantiate and move to device
model = RegressionModel(X_train.shape[1])
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.to(device)