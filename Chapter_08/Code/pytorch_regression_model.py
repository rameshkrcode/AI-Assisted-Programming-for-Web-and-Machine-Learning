
import torch.nn as nn

class RegressionModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = nn.Linear(in_features=10, out_features=1)

    def forward(self, x):
        return self.fc(x)
