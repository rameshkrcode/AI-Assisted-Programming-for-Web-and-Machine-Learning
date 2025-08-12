
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt

# Normalize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply DBSCAN
db = DBSCAN(eps=0.5, min_samples=3)
df['DBSCAN_Cluster'] = db.fit_predict(X_scaled)

# Visualize clusters
sns.scatterplot(x='Salary', y='Experience', hue='DBSCAN_Cluster', data=df, palette='tab10')
plt.title("DBSCAN Clustering")
plt.show()
