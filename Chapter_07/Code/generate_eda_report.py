
from pandas_profiling import ProfileReport
profile = ProfileReport(df, title="EDA Report", explorative=True)
profile.to_file("eda_report.html")
