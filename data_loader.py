import pandas as pd
 
def convert_sqft(x):
    try:
        if '-' in str(x):
            parts = x.split('-')
            return (float(parts[0]) + float(parts[1])) / 2
        return float(x)
    except:
        return None
 
def load_raw_data():
    df = pd.read_csv("data/raw_data.csv")
 
    # Extract BHK
    df["bhk"] = df["size"].str.extract(r'(\d+)').astype(float)
 
    # Rename column
    df.rename(columns={"total_sqft": "sqft"}, inplace=True)
 
    # Convert sqft properly
    df["sqft"] = df["sqft"].apply(convert_sqft)
 
    # Keep only required columns
    df = df[["location", "bhk", "sqft", "price"]]
 
    # Remove missing values
    df.dropna(inplace=True)
 
    return df
 
