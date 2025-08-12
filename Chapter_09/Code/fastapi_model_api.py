from fastapi import FastAPI
import torch
from pydantic import BaseModel

class Input(BaseModel):
    features: list

app = FastAPI()

model = torch.jit.load("model_scripted.pt")

@app.post("/predict")
def predict(input: Input):
    input_tensor = torch.tensor([input.features])
    output = model(input_tensor)
    return {"prediction": output.tolist()}
