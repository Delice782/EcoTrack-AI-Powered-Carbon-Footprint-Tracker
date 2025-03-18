              
import React, { useState } from "react";
import axios from "axios";

function App() {
  const [energyUsage, setEnergyUsage] = useState("");
  const [transportation, setTransportation] = useState("");
  const [foodConsumption, setFoodConsumption] = useState("");
  const [carbonFootprint, setCarbonFootprint] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.post("http://localhost:5000/predict", {
        energy_usage: energyUsage,
        transportation: transportation,
        food_consumption: foodConsumption,
      });

      setCarbonFootprint(response.data.carbon_footprint);
    } catch (error) {
      console.error("There was an error with the prediction:", error);
    }
  };

  return (
    <div className="App">
      <h1>EcoTrack: Track Your Carbon Footprint</h1>
      <form onSubmit={handleSubmit}>
        <label>
          Energy Usage (kWh):
          <input
            type="number"
            value={energyUsage}
            onChange={(e) => setEnergyUsage(e.target.value)}
          />
        </label>
        <br />
        <label>
          Transportation (km):
          <input
            type="number"
            value={transportation}
            onChange={(e) => setTransportation(e.target.value)}
          />
        </label>
        <br />
        <label>
          Food Consumption (kg CO2):
          <input
            type="number"
            value={foodConsumption}
            onChange={(e) => setFoodConsumption(e.target.value)}
          />
        </label>
        <br />
        <button type="submit">Calculate Footprint</button>
      </form>

      {carbonFootprint !== null && (
        <div>
          <h3>Your Carbon Footprint: {carbonFootprint} kg CO2</h3>
        </div>
      )}
    </div>
  );
}

export default App;
