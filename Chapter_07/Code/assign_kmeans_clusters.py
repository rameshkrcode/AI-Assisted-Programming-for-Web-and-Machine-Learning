
# Copilot auto-suggests assigning cluster labels
df['Cluster'] = KMeans(n_clusters=3, random_state=42).fit_predict(df[['Salary', 'Experience']])
