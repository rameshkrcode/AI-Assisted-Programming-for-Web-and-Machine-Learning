
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

# Select relevant features
X = df[['Salary', 'Experience']]

# Normalize the features
X_scaled = StandardScaler().fit_transform(X)

# Apply K-Means clustering
kmeans = KMeans(n_clusters=3, random_state=0)
df['Cluster'] = kmeans.fit_predict(X_scaled)

# Visualize the clusters
sns.scatterplot(x='Salary', y='Experience', hue='Cluster', data=df)
plt.title("K-Means Clustering of Employees")
plt.show()
