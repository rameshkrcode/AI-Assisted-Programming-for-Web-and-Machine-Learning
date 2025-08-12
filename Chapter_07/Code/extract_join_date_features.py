
df['JoinDate'] = pd.to_datetime(df['JoinDate'])
df['JoinYear'] = df['JoinDate'].dt.year
df['JoinMonth'] = df['JoinDate'].dt.month
df['JoinDayOfWeek'] = df['JoinDate'].dt.dayofweek
