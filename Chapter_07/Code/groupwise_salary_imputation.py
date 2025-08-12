
# Group-wise imputation using department-wise mean
df['Salary'] = df.groupby('Department')['Salary'].transform(lambda x: x.fillna(x.mean()))
