
import matplotlib.pyplot as plt
import seaborn as sns
model.fit(X, y)
importances = model.feature_importances_
sns.barplot(x=importances, y=X.columns)
plt.title("Feature Importances from Random Forest")
plt.show()
