from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# load trained model
model = joblib.load("model.pkl")
def get_aqi_category(aqi):

    if aqi <= 50:
        return "Good"

    elif aqi <= 100:
        return "Satisfactory"

    elif aqi <= 200:
        return "Moderate"

    elif aqi <= 300:
        return "Poor"

    elif aqi <= 400:
        return "Very Poor"

    else:
        return "Severe"

@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    input_data = pd.DataFrame([{
        "PM2.5": data["pm25"],
        "PM10": data["pm10"],
        "NO": data["no"],
        "NO2": data["no2"],
        "NOx": data["nox"],
        "NH3": data["nh3"],
        "CO": data["co"],
        "SO2": data["so2"],
        "O3": data["o3"]
    }])

    prediction = model.predict(input_data)[0]

    category = get_aqi_category(prediction)

    return jsonify({

    "predicted_aqi":
        round(float(prediction), 2),

    "category":
        category

})


if __name__ == "__main__":
    app.run(debug=True, port=5000)