   
import numpy as np
from sklearn.linear_model import LinearRegression
import pickle

# Example data: [energy_usage (kWh), transportation (km), food_consumption (kg CO2)]
X = np.array([
    [10, 50, 2],  # 10 kWh, 50 km, 2 kg CO2 food consumption
    [20, 100, 5],  # 20 kWh, 100 km, 5 kg CO2 food consumption
    [5, 20, 1],  # 5 kWh, 20 km, 1 kg CO2 food consumption
    [15, 70, 3],  # 15 kWh, 70 km, 3 kg CO2 food consumption
])

# Carbon footprint target (kg CO2)
y = np.array([100, 250, 50, 180])

# Train the model
model = LinearRegression()
model.fit(X, y)

# Save the trained model
with open('carbon_footprint_model.pkl', 'wb') as f:
    pickle.dump(model, f)

