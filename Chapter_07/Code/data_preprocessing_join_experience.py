
df['JoinDate'] = pd.to_datetime(df['JoinDate'], errors='coerce')
df['Experience_Level'] = df['Experience_Level'].map({'Junior': 1, 'Mid': 2, 'Senior': 3})
