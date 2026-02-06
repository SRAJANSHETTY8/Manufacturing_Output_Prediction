import streamlit as st
import requests
import pickle

st.title("Manufacturing Output Prediction")

features = pickle.load(open("../model/features.pkl","rb"))

inputs = []

for feature in features:
    val = st.number_input(feature)
    inputs.append(val)

if st.button("Predict"):

    response = requests.post(
        "https://manufacturing-output-prediction.onrender.com/predict",
        json={"data": inputs}
    )

    st.write("Prediction:", response.json())
