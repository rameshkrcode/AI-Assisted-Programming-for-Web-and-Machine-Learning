import torch
scripted_model = torch.jit.script(model)
torch.jit.save(scripted_model, "sentiment_model.pt")

@app.post("/predict")
async def predict(data: TextInput):
    tokens = tokenize(data.text)
    input_tensor = torch.tensor(tokens).unsqueeze(0)
    result = model(input_tensor)
    return {"sentiment": "positive" if result.item() > 0.5 else "negative"}