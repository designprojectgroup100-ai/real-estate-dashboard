import streamlit as st
 
def sidebar_controls(df):
    st.sidebar.title("🏠 Filters")
 
    location = st.sidebar.selectbox(
        "Location", df["location"].unique()
    )
 
    bhk = st.sidebar.selectbox("BHK", [1, 2, 3, 4])
 
    sqft = st.sidebar.slider("Area (sqft)", 500, 5000, 1000)
 
    budget = st.sidebar.slider(
        "Budget (Lakhs)", 10, 200, (30, 80)
    )
 
    return location, bhk, sqft, budget
