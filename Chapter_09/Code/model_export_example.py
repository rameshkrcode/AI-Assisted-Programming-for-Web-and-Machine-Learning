import torch

# TorchScript Conversion
scripted_model = torch.jit.script(model)
torch.jit.save(scripted_model, "model_scripted.pt")

# ONNX Export
dummy_input = torch.randn(1, 3, 224, 224)
torch.onnx.export(model, dummy_input, "model.onnx")
