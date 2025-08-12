
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())
df['JoinDate'] = pd.to_datetime(df['JoinDate'], errors='coerce')
