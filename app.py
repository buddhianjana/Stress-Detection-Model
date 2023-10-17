import streamlit as st
import pandas as pd
import joblib

# Load your trained model
log_reg = joblib.load('stress_detection.sav')  # Replace 'stress_detection.sav' with the actual path to your saved model file

# Create a Streamlit app
st.title("Stress Level Predictor")

# Add input fields for the new data
st.header("Enter New Data:")
new_data = {}
new_data["snoring_rate"] = st.number_input("snoring_rate", min_value=0.0, value=50.0, format="%.4f")
new_data["respiration_rate"] = st.number_input("respiration_rate", min_value=0.0, value=18.0, format="%.4f")
new_data["body_temperature"] = st.number_input("body_temperature", min_value=0.0, value=99.0, format="%.4f")
new_data["limb_movement"] = st.number_input("limb_movement", min_value=0.0, value=8.0, format="%.4f")
new_data["blood_oxygen"] = st.number_input("blood_oxygen", min_value=0.0, value=97.0, format="%.4f")
new_data["eye_movement"] = st.number_input("eye_movement", min_value=0.0, value=80.0, format="%.4f")
new_data["sleeping_hours"] = st.number_input("sleeping_hours", min_value=0.0, value=9.0, format="%.4f")
new_data["heart_rate"] = st.number_input("heart_rate", min_value=0.0, value=55.0, format="%.4f")

# Predict the stress level when a button is clicked
if st.button("Predict Stress Level"):
    new_data_df = pd.DataFrame([new_data])
    
    # Make the prediction using the loaded model
    predicted_stress_level = log_reg.predict(new_data_df)
    
    # Map integer stress levels to human-readable labels and associated colors
    stress_levels = {
        0: ("Low/Normal", "green"),
        1: ("Medium Low", "yellow"),
        2: ("Medium", "orange"),
        3: ("Medium High", "red"),
        4: ("High", "darkred")
    }
    
    # Get the human-readable label and color
    predicted_stress_label, label_color = stress_levels[predicted_stress_level[0]]
    
    # Style the message with different colors
    colored_text = f'<span style="color: {label_color}; font-size: 20px;">{predicted_stress_label}</span>'
    
    # Display the predicted stress level with styling
    st.markdown(colored_text, unsafe_allow_html=True)