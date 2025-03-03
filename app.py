from flask import Flask, request, jsonify
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load("xgboost_model.joblib")  # Ensure this file exists

@app.route("/")
def home():
    return "House Price Prediction API is running!"

@app.route("/predict", methods=["POST", "GET"])
def predict():
    try:
        if request.method == "GET":
            return jsonify({"message": "Use POST with JSON data to get predictions"}), 200
          
        # Get JSON request data
        data = request.get_json()
        
        # Log incoming data (for debugging)
        print("Received Data:", data)
        
        # Ensure all inputs are Python-native types to avoid float32 issues
        processed_data = {
            k: float(v) if isinstance(v, (np.float32, np.float64)) else v
            for k, v in data.items()
        }

        # Convert to DataFrame
        input_df = pd.DataFrame([processed_data])

        # Ensure column order matches the trained model
        expected_columns = [
            "median_income", "total_rooms", "housing_median_age", "latitude", "longitude",
            "ocean_proximity_INLAND", "ocean_proximity_NEAR BAY", "ocean_proximity_NEAR OCEAN",
            "ocean_proximity_ISLAND", "population", "households", "total_bedrooms",
            "bedrooms_per_household", "rooms_per_household", "population_per_household"
        ]

        # Reorder input features if needed
        input_df = input_df[expected_columns]

        # Make prediction
        prediction = model.predict(input_df)

        # Convert prediction output to a standard Python float
        result = float(prediction[0])

        return jsonify({"prediction": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 400  # Return error with HTTP 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
