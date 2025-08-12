
from sklearn.ensemble import RandomForestClassifier
import seaborn as sns
import matplotlib.pyplot as plt

model = RandomForestClassifier()
model.fit(X, y)
importances = model.feature_importances_
sns.barplot(x=importances, y=X.columns)
plt.title("Feature Importances")
plt.show()
