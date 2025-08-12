
from sklearn.metrics import davies_bouldin_score
print("DBI:", davies_bouldin_score(X, df['Cluster']))
