
# Assume df includes 'Annual Income' and 'Spending Score'
from sklearn.cluster import KMeans
import seaborn as sns
import matplotlib.pyplot as plt

X_customer = df[['Annual Income', 'Spending Score']]
kmeans = KMeans(n_clusters=4)
df['Segment'] = kmeans.fit_predict(X_customer)

sns.scatterplot(x='Annual Income', y='Spending Score', hue='Segment', data=df, palette='Set1')
plt.title("Customer Segments")
plt.show()
