
# One-hot encoding for Department
df = pd.get_dummies(df, columns=['Department'], drop_first=True)
