# Smart Greenhouse Irrigation System 🌱

## Project Overview
This project focuses on analysing greenhouse environmental data to monitor soil moisture and predict future soil moisture levels using Python and time-series forecasting.

The aim is to support smarter irrigation decisions by identifying when soil moisture falls below a specified threshold.

## Objectives
- Analyse greenhouse sensor data.
- Monitor soil moisture levels over time.
- Study the relationship between environmental parameters.
- Forecast soil moisture using the ARIMA model.
- Evaluate forecasting performance using MAE and RMSE.
- Generate insights that can support irrigation decisions.

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Statsmodels (ARIMA)

## Project Files
- `greenhouse_capstone.py` – Main Python program for data cleaning, analysis, visualisation and soil moisture forecasting.
- `texcoco_greenhouse_enriched_1week_top30 2.csv` – Greenhouse dataset used for analysis.

## How to Run the Project

1. Download or clone this repository.
2. Make sure Python is installed.
3. Install the required libraries:

   ```bash
   pip install pandas numpy matplotlib seaborn statsmodels
   ```

4. Keep the Python file and CSV dataset in the same folder.
5. Run the program:

   ```bash
   python greenhouse_capstone.py
   ```

## Methodology
1. Load and clean the greenhouse dataset.
2. Process timestamps and numerical sensor readings.
3. Analyse soil moisture and other environmental parameters.
4. Visualise trends and correlations using graphs.
5. Apply ARIMA time-series forecasting.
6. Evaluate predictions using MAE and RMSE.
7. Generate an irrigation-related alert based on the selected soil moisture threshold.

## Note
The soil moisture threshold used in the program is an illustrative value. It should be adjusted according to the crop and greenhouse requirements.

This project provides analytical predictions and decision support. It does not directly operate a physical irrigation pump or valve.

## Author
Aryan Sharma
Vega Shah

## Project
Smart Greenhouse Irrigation System
