# Smart Air Quality Monitoring System Project

## Overview

This repository contains a full-stack air quality prediction application.
It includes:
- `frontend/`: React-based UI for entering pollutant concentrations and viewing predicted AQI results.
- `backend/`: Express API server that forwards prediction requests to a machine learning prediction service and stores history in MongoDB.
- `dataset/`: Air quality dataset used for model training.
- `ml_model/`: machine learning environment folder (currently contains `venv`).

The app predicts AQI based on pollutant values and stores prediction history.

## Project Structure

- `frontend/`
  - React app created with Create React App.
  - Key components: `PredictionForm`, `History`, `AQIChart`.
  - Sends prediction requests to `http://localhost:8000/api/predict`.

- `backend/`
  - Express server in `server.js`.
  - Connects to MongoDB at `mongodb://127.0.0.1:27017/air_quality_db`.
  - Saves predicted results using `models/Prediction.js`.
  - Uses Axios to call an external ML prediction service at `http://127.0.0.1:5000/predict`.

- `dataset/`
  - Contains `Air_quality_data.csv`.

- `docs/`
  - Documentation folder for supplemental files.

- `ml_model/`
  - Contains a Python virtual environment (`venv`).
  - Add training or prediction service scripts here if needed.

## Prerequisites

- Node.js and npm
- MongoDB running locally
- A machine learning prediction service listening on `http://127.0.0.1:5000/predict`
  - The backend expects this service to return JSON with `predicted_aqi` and `category`.

## Setup

### 1. Start MongoDB

Start your local MongoDB server.

### 2. Install backend dependencies

```bash
cd backend
npm install
```

### 3. Install frontend dependencies

```bash
cd ../frontend
npm install
```

### 4. Start the backend server

```bash
cd ../backend
node server.js
```

Backend listens on port `8000`.

### 5. Start the frontend app

```bash
cd ../frontend
npm start
```

The React app will open at `http://localhost:3000`.

## Usage

1. Open the frontend in a browser.
2. Enter pollutant concentration values in the prediction form.
3. Click **Predict AQI**.
4. View the predicted AQI and category.
5. Check the prediction history section for saved results.

## API Endpoints

- `POST /api/predict`
  - Sends pollutant data to the ML prediction service.
  - Saves the response in MongoDB.

- `GET /api/history`
  - Returns stored prediction history.

## Notes

- The current backend implementation assumes the ML service is running separately on port `5000`.
- If the ML prediction service is not available, predictions will fail.
- Add your model-serving script to `ml_model/` and update the backend endpoint if needed.
