House Price Prediction API

This project provides a Flask-based API for predicting house prices using a trained XGBoost model. The model is trained on housing data with features such as median income, total rooms, housing age, location coordinates, and more. The API takes input features in JSON format and returns a predicted house price.

Features

Machine Learning Model: Trained XGBoost model to predict house prices.

Flask API: Exposes an endpoint for making predictions.

Dockerized Deployment: The API is containerized using Docker for easy deployment.

GitHub Integration: Code is version-controlled using Git and hosted on GitHub.

Project Structure

.
├── app.py                # Flask API implementation
├── xgboost_model.joblib  # Trained XGBoost model
├── requirements.txt      # Python dependencies
├── Dockerfile            # Docker configuration
├── .gitignore            # Git ignore file
├── README.md             # Project documentation
└── data/
    ├── housing.csv       # Dataset 

Installation & Setup

1. Clone the Repository

git clone https://github.com/your-username/your-repo.git
cd your-repo

2. Set Up a Virtual Environment (Optional, Recommended)

python -m venv venv
source venv/bin/activate   # On Windows, use: venv\Scripts\activate

3. Install Dependencies

pip install -r requirements.txt

4. Run the Flask API

python app.py

* The API should now be running at http://127.0.0.1:5000

API Endpoints

1. Home Endpoint

* URL: /

* Method: GET

* Response:

{"message": "House Price Prediction API is running!"}

2. Prediction Endpoint

* URL: /predict

* Method: POST

* Request Body (JSON):

{
  "median_income": 4.0,
  "total_rooms": 3000,
  "housing_median_age": 20,
  "latitude": 34.0,
  "longitude": -118.0,
  "ocean_proximity_INLAND": 1,
  "ocean_proximity_NEAR BAY": 0,
  "ocean_proximity_NEAR OCEAN": 0,
  "ocean_proximity_ISLAND": 0,
  "population": 1200,
  "households": 400,
  "total_bedrooms": 500,
  "bedrooms_per_household": 1.2,
  "rooms_per_household": 7.5,
  "population_per_household": 3.0
}

Response (JSON):

{"prediction": 228186.25}

Docker Deployment

1. Build the Docker Image

docker build -t flask-house-price-api .

2. Run the Docker Container

docker run -p 5000:5000 flask-house-price-api

* The API should now be accessible at http://localhost:5000

Pushing to GitHub

1. Initialize Git and Add Remote

git init
git remote add origin https://github.com/Saifza/flask-house-price-api

2. Commit and Push Changes

git add .
git commit -m "Initial commit"
git branch -M main
git push -u origin main

Notes

Ensure xgboost_model.joblib is included in the project folder.

Use Postman or curl to test the API.

Modify .gitignore to prevent committing unnecessary files.

License

This project is open-source and available under the MIT License.

