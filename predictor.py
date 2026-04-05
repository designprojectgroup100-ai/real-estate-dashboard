import pandas as pd
 
def predict_price(model, columns, location, bhk, sqft):
    input_df = pd.DataFrame([[location, bhk, sqft]],
                            columns=["location", "bhk", "sqft"])
 
    input_df = pd.get_dummies(input_df)
 
    input_df = input_df.reindex(columns=columns, fill_value=0)
 
    prediction = model.predict(input_df)[0]
 
    return round(prediction, 2)
