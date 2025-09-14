import streamlit as st
import pandas as pd
import numpy as np
import joblib
from datetime import datetime

# Load the trained model
model = joblib.load("regression_model.pkl")

# Page Title
st.title("Water Quality Monitoring - Dissolved Oxygen Prediction")

# Input fields for user
st.header("Enter Water Quality Parameters")

salinity = st.number_input("Salinity (ppt)", min_value=0.0, max_value=50.0, value=10.0)
ph = st.number_input("pH", min_value=0.0, max_value=14.0, value=7.0)
secchi = st.number_input("Secchi Depth (m)", min_value=0.0, max_value=20.0, value=5.0)
water_depth = st.number_input("Water Depth (m)", min_value=0.0, max_value=100.0, value=10.0)
water_temp = st.number_input("Water Temp (°C)", min_value=0.0, max_value=40.0, value=25.0)
air_temp = st.number_input("Air Temp (°C)", min_value=-10.0, max_value=50.0, value=30.0)

# Prediction
if st.button("Predict Dissolved Oxygen"):
    input_data = np.array([[salinity, ph, secchi, water_depth, water_temp, air_temp]])
    prediction = model.predict(input_data)
    st.success(f"Predicted Dissolved Oxygen: {prediction[0]:.2f} mg/L")
