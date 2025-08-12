
from sklearn.metrics import silhouette_score
score = silhouette_score(X, df['Cluster'])
print(f"Silhouette Score: {score:.2f}")
