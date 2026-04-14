import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
 
def train_model(df):
    # Convert categorical to numeric
    df = pd.get_dummies(df, columns=["location"], drop_first=True)
 
    # Features & target
    X = df.drop("price", axis=1)
    y = df["price"]
 
    # Train-Test Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
 
    # Random Forest Model
    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )
 
    # Train model
    model.fit(X_train, y_train)
 
    # Predictions for evaluation
    y_pred = model.predict(X_test)
 
    # Accuracy score
    score = r2_score(y_test, y_pred)
 
    return model, X.columns, round(score, 2)
