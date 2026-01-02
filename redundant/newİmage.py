import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('kadikoy_air_quality_2024_2025.csv', parse_dates=['time'], index_col='time')


daily = df['pm10'].resample('D').mean()
rolling = daily.rolling(window=7, center=True).mean()  

plt.figure(figsize=(12, 6))
plt.plot(daily.index, daily, alpha=0.3, color='gray', label='Daily Average (Raw)')
plt.plot(rolling.index, rolling, color='blue', linewidth=2, label='7-Day Moving Average (Trend)')
plt.title('PM10 Pollution Trend (Smoothed)', fontsize=14)
plt.ylabel('PM10 (µg/m³)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('pm10_timeseries_smoothed.png')
print("Smoothed plot saved.")