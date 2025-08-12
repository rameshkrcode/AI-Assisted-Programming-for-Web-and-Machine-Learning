
import pandas as pd
df = pd.read_csv("employee_data.csv")
print(df.isnull().sum())
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())
