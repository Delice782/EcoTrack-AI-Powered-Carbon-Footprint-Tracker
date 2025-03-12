          
from flask import Flask, request, jsonify
import numpy as np
from sklearn.linear_model import LinearRegression
import pickle

app = Flask(__name__)

# Load the pre-trained model
with open('models/carbon_footprint_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/')
def home():
    return "Welcome to EcoTrack API!"
  
@app.route('/predict', methods=['POST'])
def predict_carbon_footprint():
    try:
        data = request.get_json()
        energy_usage = data['energy_usage']  # in kWh
        transportation = data['transportation']  # in km
        food_consumption = data['food_consumption']  # in kg CO2

        # Prepare input for prediction (features)
        features = np.array([[energy_usage, transportation, food_consumption]])

        # Predict carbon footprint
        carbon_footprint = model.predict(features)

        return jsonify({'carbon_footprint': carbon_footprint[0]})
    except Exception as e:
        return jsonify({'error': str(e)}), 400
      
if __name__ == '__main__':
    app.run(debug=True)
