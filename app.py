import streamlit as st
import pandas as pd
import joblib  # To load the saved model

# Define the stress level labels
stress_level_labels = {
    0: "Low/Normal",
    1: "Medium Low",
    2: "Medium",
    3: "Medium High",
    4: "High"
}

# Load your trained model
log_reg = joblib.load('stress_detection.sav')  # Replace 'stress_detection.sav' with the actual path to your saved model file

# Create a Streamlit app
st.title("Stress Level Predictor")

# Add input fields for the new data
st.header("Enter New Data:")
new_data = {}

snoring_rate = st.text_input("snoring_rate", value="0.000")
snoring_rate = float(snoring_rate)  # Convert to float

respiration_rate = st.text_input("respiration_rate", value="0.000")
respiration_rate = float(respiration_rate)  # Convert to float

body_temperature = st.text_input("body_temperature", value="0.000")
body_temperature = float(body_temperature)  # Convert to float

limb_movemen = st.text_input("limb_movemen", value="0.000")
limb_movemen = float(limb_movemen)  # Convert to float

blood_oxygen  = st.text_input("blood_oxygen ", value="0.000")
blood_oxygen  = float(blood_oxygen )  # Convert to float

eye_movement = st.text_input("eye_movement", value="0.000")
eye_movement = float(eye_movement)  # Convert to float

sleeping_hours = st.text_input("sleeping_hours", value="0.000")
sleeping_hours = float(sleeping_hours)  # Convert to float

heart_rate  = st.text_input("heart_rate ", value="0.000")
heart_rate  = float(heart_rate )  # Convert to float


# Predict the stress level when a button is clicked
if st.button("Predict Stress Level"):
    new_data_df = pd.DataFrame([new_data])
    
    # Make the prediction using the loaded model
    predicted_stress_level = log_reg.predict(new_data_df)
    
    # Get the human-readable label
    predicted_stress_label = stress_level_labels[predicted_stress_level[0]]
    
    # Display the result
    st.write(f"Predicted Stress Label: {predicted_stress_level[0]} ({predicted_stress_label})")