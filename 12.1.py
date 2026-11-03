
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller


df = pd.read_csv("flights.csv")

df['Date'] = pd.to_datetime(
    df['year'].astype(str) + '-' + df['month'].astype(str)
)

df.set_index('Date', inplace=True)

ts = df['passengers']

plt.figure(figsize=(12, 5))
plt.plot(ts, label='Monthly Passengers')
plt.title('Monthly Airline Passengers (1949-1960)')
plt.xlabel('Year')
plt.ylabel('Number of Passengers')
plt.legend()
plt.grid()
plt.show()

rolling_mean = ts.rolling(window=12).mean()
rolling_std = ts.rolling(window=12).std()

plt.figure(figsize=(12, 5))
plt.plot(ts, label='Original Series')
plt.plot(rolling_mean, label='12-Month Rolling Mean')
plt.plot(rolling_std, label='12-Month Rolling Standard Deviation')
plt.title('Rolling Mean and Standard Deviation')
plt.xlabel('Year')
plt.ylabel('Passengers')
plt.legend()
plt.grid()
plt.show()

def adf_test(series):
    result = adfuller(series.dropna())

    print("\nADF Test Results")
    print("ADF Statistic:", result[0])
    print("p-value:", result[1])

    if result[1] <= 0.05:
        print("Conclusion: Series is STATIONARY")
        return True
    else:
        print("Conclusion: Series is NON-STATIONARY")
        return False

print("Original Series:")
stationary = adf_test(ts)

diff_series = ts.copy()
d = 0

while not stationary and d < 2:
    diff_series = diff_series.diff().dropna()
    d += 1

    print(f"\nAfter {d} Order Differencing:")
    stationary = adf_test(diff_series)

plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(ts)
plt.title('Original Time Series')
plt.ylabel('Passengers')
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(diff_series)
plt.title(f'Final Differenced Series (d={d})')
plt.xlabel('Year')
plt.ylabel('Differenced Passengers')
plt.grid()

plt.tight_layout()
plt.show()

print("\nFinal Result")
print("Order of Differencing:", d)

if stationary:
    print("The series is stationary after differencing.")
else:
    print("The series is still non-stationary after 2 differences.")
