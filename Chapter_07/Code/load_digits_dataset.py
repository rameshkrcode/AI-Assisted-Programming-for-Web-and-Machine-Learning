
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt

digits = load_digits()
X = digits.data             # Flattened 64-pixel feature vectors
images = digits.images      # Original 8x8 image format
