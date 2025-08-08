import pandas as pd
# Load access logs from a CSV file
logs = pd.read_csv("access_logs.csv")
# Detect IPs with multiple failed login attempts
failed_logins = logs[(logs["status"] == "failed")].groupby("ip").count()
# Flag IPs with more than 10 failed login attempts as suspicious
suspicious_ips = failed_logins[failed_logins["status"] > 10]
# Print suspicious IPs
print("Suspicious Login Attempts:")
print(suspicious_ips)
