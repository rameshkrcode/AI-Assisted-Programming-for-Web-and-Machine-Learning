
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
# Load and scale data
df = pd.read_csv("employee_data.csv")
X = df[['Salary', 'Experience']]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
# Fit K-Means
kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(X_scaled)
# Evaluate
score = silhouette_score(X_scaled, df['Cluster'])
print(f"Silhouette Score: {score:.2f}")
# Visualize
sns.scatterplot(x='Salary', y='Experience', hue='Cluster', data=df)
plt.title("Employee Clustering")
plt.show()
