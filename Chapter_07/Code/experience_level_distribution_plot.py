
import matplotlib.pyplot as plt
df['Experience_Level'].value_counts().plot(kind='bar')
plt.title("Distribution of Experience Levels")
plt.show()
