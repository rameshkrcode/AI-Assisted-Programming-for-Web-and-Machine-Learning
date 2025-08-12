
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df['Experience_Level'] = le.fit_transform(df['Experience_Level'])
