import pandas as pd
 
def load_raw_data():
    return pd.read_csv("data/raw_data.csv")
 
def preprocess_data(df):
    df = df.copy()
 
    # Basic cleaning (you can expand later)
    df = df.dropna()
 
    # Save processed data
    df.to_csv("data/processed_data.csv", index=False)
 
    return df
 
