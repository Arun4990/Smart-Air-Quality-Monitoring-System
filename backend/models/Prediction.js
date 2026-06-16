const mongoose = require("mongoose");

const predictionSchema = new mongoose.Schema({

  pm25: Number,
  pm10: Number,
  no: Number,
  no2: Number,
  nox: Number,
  nh3: Number,
  co: Number,
  so2: Number,
  o3: Number,

  predictedAQI: Number,
category: String,
  createdAt: {
    type: Date,
    default: Date.now
  }

});

module.exports = mongoose.model(
  "Prediction",
  predictionSchema
);