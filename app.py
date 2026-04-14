import streamlit as st
 
from data_loader import load_raw_data, preprocess_data
from sidebar import sidebar_controls
from model import train_model
from predictor import predict_price
 
st.set_page_config(page_title="Real Estate Analyzer", layout="wide")
 
st.title("🏡 Indian Real Estate Price Analyzer")
st.subheader("📊 Model Performance")
st.write(f"R² Score: {score}")
 
 
# Load & preprocess data
df = load_raw_data()
df = preprocess_data(df)
 
# Sidebar
location, bhk, sqft, budget = sidebar_controls(df)
 
# Train model
model, columns, score = train_model(df)
 
# Prediction
price = predict_price(model, columns, location, bhk, sqft)
 
# Output
st.subheader("💰 Estimated Price")
st.metric(label="Predicted Price", value=f"₹ {price} Lakhs")
 
# Budget logic
if budget[0] <= price <= budget[1]:
    st.success("✅ Fits your budget")
else:
    st.warning("⚠️ Not in your budget")
 
# Visualization
st.subheader("📊 Price vs Area")
st.scatter_chart(df[["sqft", "price"]])
 
