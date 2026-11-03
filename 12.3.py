import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima.model import ARIMA

weekly = sm.datasets.co2.load_pandas().data["co2"]
monthly = weekly.resample("MS").mean().interpolate(method="time")
print("Monthly averages regularize the weekly data; interpolation fills missing months.")
print("Additive decomposition suits approximately constant seasonal amplitude.")
decomposition = seasonal_decompose(monthly, model="additive", period=12)
fig = decomposition.plot()
fig.set_size_inches(12, 9)
plt.tight_layout()
plt.show()

adjusted = monthly - decomposition.seasonal
working = adjusted.copy()
d = 0

while True:
    result = adfuller(working.dropna(), autolag="AIC")
    print(f"ADF p-value at difference order {d}: {result[1]}")
    if result[1] < 0.05:
        break
    if d == 2:
        raise ValueError("Stationarity was not established after two differences.")
    working = working.diff().dropna()
    d += 1

trend = "t" if d == 1 else "c" if d == 0 else "n"
candidates = []
for p, q in [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)]:
    try:
        fitted = ARIMA(adjusted, order=(p, d, q), trend=trend).fit()

        if fitted.mle_retvals.get("converged", True) and np.isfinite(fitted.aic):
            candidates.append((fitted.aic, (p, d, q), fitted))
    except (ValueError, np.linalg.LinAlgError):
        continue

if not candidates:
    raise RuntimeError("No model converged.")

candidates.sort(key=lambda item: item[0])
best_aic, best_order, model = candidates[0]
print("\nSelected ARIMA order:", best_order)
print("ADF selects d; the lowest AIC among converged candidates selects p and q.")
print("Annual seasonality is removed before ARIMA and restored afterward.")

if d == 1:
    print("A drift term models the upward trend.")

print(model.summary())
prediction = model.get_forecast(steps=24)
adjusted_forecast = prediction.predicted_mean
pattern = decomposition.seasonal.groupby(
    decomposition.seasonal.index.month
).mean()

seasonality = pd.Series(
    [pattern.loc[date.month] for date in adjusted_forecast.index],
    index=adjusted_forecast.index
)

forecast = adjusted_forecast + seasonality
interval = prediction.conf_int()
lower = interval.iloc[:, 0] + seasonality
upper = interval.iloc[:, 1] + seasonality
print("\n24-Month Forecast:")
print(forecast.round(2))
plt.figure(figsize=(12, 6))
plt.plot(monthly, label="Historical")
plt.plot(forecast, color="red", label="Forecast")
plt.fill_between(
    forecast.index,
    lower.to_numpy(),
    upper.to_numpy(),
    color="red",
    alpha=0.2,
    label="95% Conditional Forecast Interval"
)
plt.title("Atmospheric CO2 Forecast")
plt.xlabel("Year")
plt.ylabel("CO2 (ppm)")
plt.legend()
plt.tight_layout()
plt.show()

if adjusted_forecast.iloc[-1] > adjusted.iloc[-1]:
    print("The long-term upward trend continues in the forecast.")
else:
    print("The long-term upward trend does not continue in the forecast.")

print("Forecast intervals treat estimated seasonality as fixed.")