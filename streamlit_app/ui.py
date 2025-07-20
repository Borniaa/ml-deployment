import streamlit as st
import pandas as pd
from app.predict import predict_potability

st.title("💧 Water Potability Prediction App")
st.markdown("Enter the water properties below:")

features = []
feature_names = [
    "pH", "Hardness", "Solids", "Chloramines", "Sulfate",
    "Conductivity", "Organic_carbon", "Trihalomethanes", "Turbidity"
]

for name in feature_names:
    value = st.number_input(f"{name}:", min_value=0.0, step=0.1)
    features.append(value)

if st.button("Predict"):
    result = predict_potability(features)
    if result == 1:
        st.success("✅ The water is **potable**.")
    else:
        st.error("❌ The water is **not potable**.")
import streamlit as st

st.title("Water Potability Predictor")
st.write("Upload your data and get predictions")
def main():
    st.title("Water Potability Predictor")
    st.write("Upload your data and get predictions")

    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("Data Preview:", df.head())
        
        if st.button("Predict Potability"):
            predictions = predict_potability(df)
            st.write("Predictions:", predictions)
