
# Copilot auto-suggests scaling before applying DBSCAN
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN
X_scaled = StandardScaler().fit_transform(df[['Salary', 'Experience']])
df['DBSCAN_Cluster'] = DBSCAN(eps=0.3, min_samples=4).fit_predict(X_scaled)
