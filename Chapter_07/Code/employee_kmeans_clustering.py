
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

# Clustering based on salary and experience
X = df[['Salary', 'Experience']]
kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(X)

sns.scatterplot(x='Salary', y='Experience', hue='Cluster', data=df, palette='Set2')
plt.title("K-Means Clustering of Employees")
plt.show()
