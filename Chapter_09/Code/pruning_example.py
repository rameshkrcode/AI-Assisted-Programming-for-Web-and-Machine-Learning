import torch.nn.utils.prune as prune
prune.l1_unstructured(model.fc, name="weight", amount=0.3)
