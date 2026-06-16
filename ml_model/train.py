import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error
import joblib

# Load dataset
df = pd.read_csv("../../dataset/Air_quality_data.csv")

# Select features
X = df[
    [
        "PM2.5",
        "PM10",
        "NO",
        "NO2",
        "NOx",
        "NH3",
        "CO",
        "SO2",
        "O3"
    ]
]

# Target
y = df["AQI"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = RandomForestRegressor(
    n_estimators=20,
    max_depth=5,
    random_state=42
)

model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Accuracy
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

print("R2 Score:", r2)
print("Mean Absolute Error:", mae)

# Save model
joblib.dump(model, "model.pkl")

print("Model saved as model.pkl")