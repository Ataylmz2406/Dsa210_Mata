from datetime import datetime
from meteostat import Point, Hourly

start = datetime(2024, 10, 3) 

end = datetime(2025, 11, 28, 23, 59)

# Kadıköy 
location = Point(40.990, 29.025, 30)

print(f"Fetching weather data from {start.date()} to {end.date()}")
data = Hourly(location, start, end)
data = data.fetch()

# Rename columns
data = data.rename(columns={
    'temp': 'temperature',
    'rhum': 'humidity',
    'prcp': 'precipitation',
    'wspd': 'wind_speed',
    'wdir': 'wind_direction'
})

# Filter
weather_df = data[['temperature', 'humidity', 'precipitation', 'wind_speed', 'wind_direction']]
# save to CSV
weather_df.to_csv('kadikoy_weather_2024_2025.csv')
print(f"Weather data saved: {len(weather_df)} rows to 'kadikoy_weather_2024_2025.csv'.")