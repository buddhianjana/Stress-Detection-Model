import streamlit as st
import pandas as pd
import joblib

# Define the stress level labels
stress_level_labels = {
    0: "Low/Normal",
    1: "Medium Low",
    2: "Medium",
    3: "Medium High",
    4: "High"
}

# Load your trained model and necessary data (Replace placeholders with actual model and data)
model = joblib.load('StressDetection.sav')  # Load your trained model
# Example: X = load_data()

# Set the page title and icon
st.set_page_config(
    page_title="Stress Level Predictor",
    page_icon=":chart_with_upwards_trend:"
)

# Create a Streamlit app with a centered layout
st.title("Stress Level Predictor")
st.markdown("---")

# Add input fields for the new data
st.header("Enter New Data:")

new_data = {}

snoring_rate = st.text_input("Snoring Rate", value="0.000")
snoring_rate = float(snoring_rate)  # Convert to float

# (Repeat the above input fields for other features)

# Predict the stress level when a button is clicked
if st.button("Predict Stress Level"):
    new_data_df = pd.DataFrame([new_data])
    
    # Make the prediction using your model
    predicted_stress_level = model.predict(new_data_df)
    
    # Get the human-readable label
    predicted_stress_label = stress_level_labels[predicted_stress_level[0]]
    
    # Display the result
    st.markdown("---")
    st.subheader("Prediction Result")
    st.write(f"Predicted Stress Level: {predicted_stress_label}")

# Add some additional styling using CSS
st.markdown(
    """
    <style>
    /* Center the Streamlit app */
    .stApp {
        max-width: 800px;
        margin: 0 auto;
    }

    /* Style the input fields */
    .stTextInput {
        width: 100%;
    }

    /* Style the button */
    .stButton button {
        background-color: #008C76;
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }

    /* Style the button on hover */
    .stButton button:hover {
        background-color: #006851;
    }

    /* Style the header */
    .st-eb {
        font-size: 18px;
        font-weight: bold;
    }

    /* Style the subheader */
    .st-e9 {
        font-size: 16px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
