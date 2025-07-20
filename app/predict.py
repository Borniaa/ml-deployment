import joblib
import numpy as np

# Load model and scaler
model = joblib.load('app/rf.pkl')
scaler = joblib.load('app/scaler.pkl')

def predict_potability(features: list):
    data = np.array(features).reshape(1, -1)
    data_scaled = scaler.transform(data)
    
    prediction = model.predict(data_scaled)
    return int(prediction[0])
