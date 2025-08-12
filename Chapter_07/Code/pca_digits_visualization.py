
from sklearn.decomposition import PCA
import seaborn as sns
import matplotlib.pyplot as plt

X_pca = PCA(n_components=2).fit_transform(X)
sns.scatterplot(x=X_pca[:, 0], y=X_pca[:, 1], hue=labels, palette='tab10')
plt.title("Digit Clusters via PCA")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.show()
