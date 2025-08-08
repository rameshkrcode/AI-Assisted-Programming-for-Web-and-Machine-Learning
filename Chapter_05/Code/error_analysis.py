import pandas as pd
# Load server logs
logs = pd.read_csv("server_logs.csv")
# Detect frequent error messages
error_counts = logs[logs["status"] == "error"]["message"].value_counts()
# Display the most common errors
print("Most Frequent Errors:")
print(error_counts.head(5))