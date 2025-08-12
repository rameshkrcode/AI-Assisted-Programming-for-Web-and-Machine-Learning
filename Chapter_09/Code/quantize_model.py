import torch
from torch.quantization import quantize_dynamic
quantized_model = quantize_dynamic(
    model, {torch.nn.Linear}, dtype=torch.qint8
)
torch.save(quantized_model, "quantized_model.pt")