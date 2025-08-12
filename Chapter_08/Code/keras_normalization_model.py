
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Normalization, Dense

normalizer = Normalization()
normalizer.adapt(X_train)

model = Sequential([
    normalizer,
    Dense(64, activation='relu'),
    Dense(1, activation='sigmoid')
])
