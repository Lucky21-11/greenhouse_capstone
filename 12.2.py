
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

df = pd.read_csv("flights.csv")

df['Date'] = pd.to_datetime(
    df['year'].astype(str) + '-' + df['month'].astype(str)
)

df.set_index('Date', inplace=True)

ts = df['passengers']

sma = ts.rolling(window=12).mean()
ewma = ts.ewm(span=12, adjust=False).mean()

plt.figure(figsize=(12, 5))
plt.plot(ts, label='Original Series')
plt.plot(sma, label='12-Month Simple Moving Average')
plt.plot(ewma, label='Exponentially Weighted Moving Average')

plt.title('SMA and EWMA Comparison')
plt.xlabel('Year')
plt.ylabel('Passengers')
plt.legend()
plt.grid()
plt.show()

print("EWMA follows recent changes more responsively than SMA.")

result = seasonal_decompose(ts, model='multiplicative', period=12)

result.plot()
plt.suptitle('Multiplicative Seasonal Decomposition', fontsize=14)
plt.tight_layout()
plt.show()

seasonal_effect = result.seasonal.groupby(result.seasonal.index.month).mean()

month_names = [
    'January', 'February', 'March', 'April',
    'May', 'June', 'July', 'August',
    'September', 'October', 'November', 'December'
]

seasonal_effect.index = month_names

print("\nAverage Seasonal Effect for Each Month:")
print(seasonal_effect)

print("\nHighest Air Travel Month:")
print(seasonal_effect.idxmax())

print("\nLowest Air Travel Month:")
print(seasonal_effect.idxmin())
