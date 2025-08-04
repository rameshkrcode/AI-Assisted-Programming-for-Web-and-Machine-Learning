
from pandas_profiling import ProfileReport
import pandas as pd

df = pd.read_csv("data.csv")
profile = ProfileReport(df, title="Data Profile")
profile.to_notebook_iframe()
