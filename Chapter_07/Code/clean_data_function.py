
def clean_data(df):
    df.dropna(inplace=True)
    df['JoinDate'] = pd.to_datetime(df['JoinDate'], errors='coerce')
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    return df
