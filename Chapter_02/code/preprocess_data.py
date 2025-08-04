
def preprocess_data(data):
    data = data.dropna()
    data = data.apply(lambda x: x.lower() if isinstance(x, str) else x)
    return data
