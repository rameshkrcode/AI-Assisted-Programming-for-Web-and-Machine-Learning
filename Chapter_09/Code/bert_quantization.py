from transformers import BertModel
import torch
from torch.quantization import quantize_dynamic
# Load pretrained BERT model
model = BertModel.from_pretrained('bert-base-uncased')
# Apply dynamic quantization to Linear layers
quantized_model = quantize_dynamic(
    model, {torch.nn.Linear}, dtype=torch.qint8
)
# Save quantized model
torch.save(quantized_model.state_dict(), 'bert_quantized.pth')