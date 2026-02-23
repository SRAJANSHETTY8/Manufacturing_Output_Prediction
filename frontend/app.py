import streamlit as st
import requests
import pickle
import os

# Page configuration
st.set_page_config(
    page_title="Manufacturing Capacity Predictor",
    layout="wide"
)

# Header Section
st.markdown(
    """
    <h1 style='text-align: center;'>Manufacturing Output Prediction System</h1>
    <p style='text-align: center;'>AI-Based Machine Production Capacity Estimator</p>
    """,
    unsafe_allow_html=True
)

st.divider()

# Load features safely
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
features = pickle.load(open(os.path.join(BASE_DIR, "model", "features.pkl"), "rb"))

# Sidebar Input Panel
st.sidebar.header("Machine Parameters")
inputs = []

for feature in features:
    value = st.sidebar.number_input(
        feature.replace("_", " "),
        min_value=0.0,
        value=0.0
    )
    inputs.append(value)

# Prediction Section
st.subheader("Prediction Result")

if st.button("Predict Production Capacity"):

    with st.spinner("Analyzing machine parameters..."):
        response = requests.post(
            "https://manufacturing-output-prediction.onrender.com/predict",
            json={"data": inputs}
        )

    if response.status_code == 200:
        result = response.json()
        prediction_value = result["prediction"]

        col1, col2, col3 = st.columns(3)

        with col2:
            st.metric(
                label="Predicted Output (Parts per Hour)",
                value=f"{prediction_value:.2f}"
            )

        st.divider()

        if prediction_value < 50:
            st.error("Production Level: Low Capacity")
        elif prediction_value < 200:
            st.warning("Production Level: Moderate Capacity")
        else:
            st.success("Production Level: High Capacity")

    else:
        st.error("Server is waking up or an error occurred. Please try again.")