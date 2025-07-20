import streamlit as st
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
