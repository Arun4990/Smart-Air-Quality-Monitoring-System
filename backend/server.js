const express = require("express");
const axios = require("axios");
const cors = require("cors");
const connectDB = require("./db");
const Prediction = require("./models/Prediction");

connectDB();
const app = express();

app.use(cors());
app.use(express.json());


// route
app.post("/api/predict", async (req, res) => {
  try {
    const response = await axios.post(
      "http://127.0.0.1:5000/predict",
      req.body
    );

    const newPrediction = new Prediction({
      ...req.body,
      predictedAQI: response.data.predicted_aqi,
      category: response.data.category,
    });

    await newPrediction.save();

    res.json({
      success: true,
      predictedAQI: response.data.predicted_aqi,
      category: response.data.category,
    });
  } catch (error) {
  console.error("Error:", error);
  console.error("Response:", error.response?.data);

  res.status(500).json({
    error: error.message
  });
}
});
app.get("/api/history", async (req, res) => {

  const data = await Prediction.find();

  res.json(data);

});

app.listen(8000, () => {
  console.log("Backend running on port 8000");
});