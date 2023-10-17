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
new_data["Feature 1"] = st.number_input("Feature 1", min_value=0, value=50)
new_data["Feature 2"] = st.number_input("Feature 2", min_value=0, value=18)
new_data["Feature 3"] = st.number_input("Feature 3", min_value=0, value=99)
new_data["Feature 4"] = st.number_input("Feature 4", min_value=0, value=8)
new_data["Feature 5"] = st.number_input("Feature 5", min_value=0, value=97)
new_data["Feature 6"] = st.number_input("Feature 6", min_value=0, value=80)
new_data["Feature 7"] = st.number_input("Feature 7", min_value=0, value=9)
new_data["Feature 8"] = st.number_input("Feature 8", min_value=0, value=55)

# Predict the stress level when a button is clicked
if st.button("Predict Stress Level"):
    new_data_df = pd.DataFrame([new_data])
    
    # Make the prediction using the loaded model
    predicted_stress_level = log_reg.predict(new_data_df)
    
    # Get the human-readable label
    predicted_stress_label = stress_level_labels[predicted_stress_level[0]]
    
    # Display the result
    st.write(f"Predicted Stress Label: {predicted_stress_level[0]} ({predicted_stress_label})")