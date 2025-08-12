
import seaborn as sns
import matplotlib.pyplot as plt
sns.boxplot(x='Department', y='Salary', data=df)
plt.title("Salary by Department")
plt.show()
