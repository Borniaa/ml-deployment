import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import joblib

# Load and prepare data
df = pd.read_csv('water_potability.csv')
df.fillna(df.median(), inplace=True)

X = df.drop(columns='Potability')
y = df['Potability']

X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

# Train and save model
model = RandomForestClassifier(random_state=42)
model.fit(X_train_scaled, y_train)

joblib.dump(model, 'app/rf.pkl')
joblib.dump(scaler, 'app/scaler.pkl')
