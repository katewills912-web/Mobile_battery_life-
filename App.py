import streamlit as st
import numpy as np
import joblib


# Load the trained model
model = joblib.load("Mobilebatteryhealth_model.pkl")

st.title("📱 Mobile Battery Life Predictor")

# User Inputs
user_name = st.text_input("Enter your name")
battery_capacity = st.number_input("Battery Capacity (mAh)", 2800, 6000, 4000)
screen_size = st.number_input("Screen Size (inches)", 4.5, 7.0, 6.0)
daily_usage = st.number_input("Daily Usage (hours)", 1, 12, 5)

if st.button("Predict Battery Life"):
    input_data = np.array([[battery_capacity, screen_size, daily_usage]])
    prediction = model.predict(input_data).item()
    st.success(f"Hello {user_name}! 🔋 Predicted Battery Life: {prediction:.2f} Hours")


