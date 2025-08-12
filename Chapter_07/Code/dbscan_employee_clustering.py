
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt

# Select and scale features
X = df[['Salary', 'Experience']]
X_scaled = StandardScaler().fit_transform(X)

# Apply DBSCAN
dbscan = DBSCAN(eps=0.5, min_samples=5)
df['Cluster'] = dbscan.fit_predict(X_scaled)

# Visualize the clusters
sns.scatterplot(x='Salary', y='Experience', hue='Cluster', data=df, palette='tab10')
plt.title("DBSCAN Clustering")
plt.show()
