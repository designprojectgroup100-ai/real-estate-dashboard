import pandas as pd
 
def load_raw_data():
    df = pd.read_csv("data/raw_data.csv")
 
    # Extract BHK from 'size'
    df["bhk"] = df["size"].str.extract(r'(\d+)').astype(float)
 
    # Rename columns
    df.rename(columns={
        "total_sqft": "sqft"
    }, inplace=True)
 
    # Keep only needed columns
    df = df[["location", "bhk", "sqft", "price"]]
 
    # Drop missing values
    df.dropna(inplace=True)
 
    return df
