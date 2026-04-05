import pandas as pd
from sklearn.linear_model import LinearRegression
 
def train_model(df):
    df = pd.get_dummies(df, columns=["location"], drop_first=True)
 
    X = df.drop("price", axis=1)
    y = df["price"]
 
    model = LinearRegression()
    model.fit(X, y)
 
    return model, X.columns
