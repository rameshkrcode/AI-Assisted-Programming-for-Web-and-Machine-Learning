
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import seaborn as sns
import matplotlib.pyplot as plt

# Apply K-Means clustering
kmeans = KMeans(n_clusters=2, random_state=42)
labels = kmeans.fit_predict(X.toarray())

# Reduce dimensionality for visualization
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X.toarray())

# Plot the clusters
sns.scatterplot(x=X_pca[:, 0], y=X_pca[:, 1], hue=labels)
plt.title("Clustering of Text Reviews")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.show()
