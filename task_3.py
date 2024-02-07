from fastapi import FastAPI
from typing import Optional
from datetime import datetime
import pandas as pd
import joblib
import uvicorn
from typing import Optional, Dict, Any


# Paths
FILE_PATH = "data/hurricanes_per_year.csv"
MODEL_PATH = "models/SARIMA_model.pkl"

# Load the trained model
SARIMAX_model = joblib.load(MODEL_PATH)

# Function to get the forecast
def get_forecast(model, data, year: int = 2016) -> int:
    """
    Get the forecast for the specified year.

    Args:
    - model: The trained SARIMAX model.
    - data: DataFrame containing hurricane data.
    - year (int): The year to get the forecast for.

    Returns:
    - int: The forecasted number of hurricanes.
    """
    n_periods = year - max(data.index.year)

    fitted, confint = model.predict(n_periods=n_periods, return_conf_int=True)
    index_of_fc = pd.date_range(data.index[-1] + pd.DateOffset(years=1), periods=n_periods, freq='Y')

    # Создание серии для целей построения графика
    fitted_series = pd.Series(fitted.values, index=index_of_fc)

    return int(fitted_series[fitted_series.index.year == year].values[0])


# Create an instance of FastAPI
app = FastAPI()

# Read hurricane data from CSV
hurricanes_per_year = pd.read_csv(FILE_PATH, index_col=0, parse_dates=True)

# Define route to handle requests
@app.get("/forecast/")
async def forecast(year: int) -> Dict[str, Any]:
    """
    Endpoint to get the forecasted number of hurricanes for a given year.

    Args:
    - year (int): The year to get the forecast for.

    Returns:
    - dict: A dictionary containing the year and the forecasted number of hurricanes.
    """
    if year <= 2015:
        result = int(hurricanes_per_year[hurricanes_per_year.index.year == 2008].values[0][0])
        return {"Attention": "If you need a forecast, the year must be after 2015",
                "year": year,
                "number_of_hurricanes": result
                }
    # Get the forecast for the specified year
    result = get_forecast(SARIMAX_model, hurricanes_per_year, year)
    return {"year": year, 
            "forecasted_hurricanes": result}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
    