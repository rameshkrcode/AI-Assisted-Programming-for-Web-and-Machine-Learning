
from sklearn.neighbors import NearestNeighbors
import numpy as np
import matplotlib.pyplot as plt

neighbors = NearestNeighbors(n_neighbors=5)
neighbors_fit = neighbors.fit(X_scaled)
distances, indices = neighbors_fit.kneighbors(X_scaled)

# Sort and plot the distances to the 5th nearest neighbor
distances = np.sort(distances[:, 4], axis=0)
plt.plot(distances)
plt.title("k-distance Graph")
plt.ylabel("Distance to 5th Nearest Neighbor")
plt.xlabel("Sorted Points")
plt.show()
